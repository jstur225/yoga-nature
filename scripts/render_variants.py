"""本地合成：把自然物（上）与体式（下）拼成 3:4 黑白对照图。

用法：
    python render_variants.py nature.png pose_clean.png final.png

固定规则：
    - 画布 1080x1440（3:4）
    - 上块放自然物，下块放体式
    - 中间 1px 细分割线
    - 整图转灰度（纯黑白）
"""
import argparse
import sys

try:
    from PIL import Image
except ImportError:
    sys.exit("缺少 Pillow，请先运行: pip install -r requirements.txt")

W, H = 1080, 1440
HALF = H // 2
MARGIN = 24  # 图片距边缘留白
SEPARATOR = 2  # 分割线宽度（px）


def fit_contain(img, box):
    """等比缩放图片使其完全放进 box 内，返回缩放后的图。"""
    img = img.copy()
    img.thumbnail(box)
    return img


def center_paste(canvas, img, cx, cy):
    """把 img 以 (cx, cy) 为中心贴到 canvas 上。"""
    x = int(cx - img.width / 2)
    y = int(cy - img.height / 2)
    canvas.paste(img, (x, y))


def compose(nature_path, pose_path, out_path):
    nature = Image.open(nature_path).convert("L")
    pose = Image.open(pose_path).convert("L")

    # 白底画布
    canvas = Image.new("L", (W, H), 255)

    # 上半块：自然物（居中）
    box_top = (W - 2 * MARGIN, HALF - 2 * MARGIN)
    n_fit = fit_contain(nature, box_top)
    center_paste(canvas, n_fit, W // 2, HALF // 2)

    # 下半块：体式（居中）
    box_bottom = (W - 2 * MARGIN, HALF - 2 * MARGIN)
    p_fit = fit_contain(pose, box_bottom)
    center_paste(canvas, p_fit, W // 2, HALF + (HALF // 2))

    # 中间分割线
    for y in range(HALF - SEPARATOR // 2, HALF + SEPARATOR // 2 + 1):
        if 0 <= y < H:
            canvas.paste(0, (0, y, W, y + 1))

    canvas.save(out_path, "PNG")
    print(f"已合成: {out_path} ({W}x{H} 黑白)")


def main():
    p = argparse.ArgumentParser(prog="render_variants")
    p.add_argument("nature", help="自然物图片（上半块）")
    p.add_argument("pose", help="体式图片（下半块）")
    p.add_argument("out", help="输出 PNG 路径")
    args = p.parse_args()
    compose(args.nature, args.pose, args.out)


if __name__ == "__main__":
    main()
