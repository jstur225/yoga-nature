"""Gemini 2.5 Flash Image 封装：生图 + 原片黑白化。

用法：
    python gemini_img.py generate "提示词" out.png
    python gemini_img.py generate --prompt-file prompt.txt out.png
    python gemini_img.py clean in.jpg out.png

自动读取 modlens 的 gemini key（~/.modlens/config.json），
自动走 Windows 系统代理（注册表 ProxyServer），可用环境变量覆盖：
    GEMINI_API_KEY、GEMINI_PROXY
"""
import argparse
import base64
import io
import json
import os
import sys

try:
    import requests
except ImportError:
    sys.exit("缺少 requests，请先运行: pip install -r requirements.txt")

try:
    from PIL import Image
except ImportError:
    sys.exit("缺少 Pillow，请先运行: pip install -r requirements.txt")

# 可用环境变量 GEMINI_MODEL 覆盖（不同档位/服务可用模型不同）
MODEL = os.environ.get("GEMINI_MODEL", "gemini-2.5-flash-image")
if MODEL == "gemini-3.1-flash-image":
    sys.exit(
        "本项目禁用 gemini-3.1-flash-image；请使用 gemini-2.5-flash-image。"
    )
ENDPOINT = (
    "https://generativelanguage.googleapis.com/v1beta/models/"
    f"{MODEL}:generateContent"
)
MODLENS_CONFIG = os.path.join(os.path.expanduser("~"), ".modlens", "config.json")
MAX_EDGE = 1536  # 输入图片最长边限制，超过则缩小


def get_api_key():
    if os.environ.get("GEMINI_API_KEY"):
        return os.environ["GEMINI_API_KEY"]
    if os.path.exists(MODLENS_CONFIG):
        try:
            with open(MODLENS_CONFIG, encoding="utf-8") as f:
                cfg = json.load(f)
            key = cfg.get("providers", {}).get("gemini-api", {}).get("apiKey")
            if key:
                return key
        except Exception:
            pass
    sys.exit("未找到 Gemini key。请设置环境变量 GEMINI_API_KEY，或配置 modlens。")


def get_proxy():
    if os.environ.get("GEMINI_PROXY"):
        return os.environ["GEMINI_PROXY"]
    try:
        import winreg

        k = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Software\Microsoft\Windows\CurrentVersion\Internet Settings",
        )
        enable, _ = winreg.QueryValueEx(k, "ProxyEnable")
        server, _ = winreg.QueryValueEx(k, "ProxyServer")
        winreg.CloseKey(k)
        if enable and server:
            if not server.startswith("http"):
                server = "http://" + server
            return server
    except Exception:
        pass
    return None  # 直连


def image_to_png_b64(path):
    """读取图片，统一转 PNG 并 base64，超长边自动缩小。"""
    img = Image.open(path).convert("RGB")
    if max(img.size) > MAX_EDGE:
        img.thumbnail((MAX_EDGE, MAX_EDGE))
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    return base64.b64encode(buf.getvalue()).decode("ascii")


def call_gemini(prompt, input_b64=None):
    parts = []
    if input_b64:
        parts.append({"inline_data": {"mime_type": "image/png", "data": input_b64}})
    parts.append({"text": prompt})

    body = {
        "contents": [{"parts": parts}],
        "generationConfig": {"responseModalities": ["IMAGE"]},
    }

    proxy = get_proxy()
    proxies = {"http": proxy, "https": proxy} if proxy else None
    r = requests.post(
        ENDPOINT,
        params={"key": get_api_key()},
        headers={"Content-Type": "application/json"},
        json=body,
        proxies=proxies,
        timeout=240,
    )
    if r.status_code != 200:
        sys.exit(f"Gemini API {r.status_code}: {r.text[:600]}")

    data = r.json()
    try:
        for part in data["candidates"][0]["content"]["parts"]:
            if "inlineData" in part:
                return part["inlineData"]["data"], part["inlineData"].get(
                    "mimeType", "image/png"
                )
    except (KeyError, IndexError):
        pass
    sys.exit("Gemini 响应中没有图片: " + json.dumps(data, ensure_ascii=False)[:600])


def save_b64(b64, mime, out_path):
    img_bytes = base64.b64decode(b64)
    img = Image.open(io.BytesIO(img_bytes))
    img.convert("RGB").save(out_path, "PNG")
    print(f"已保存: {out_path}")


def cmd_generate(args):
    prompt = (
        open(args.prompt, encoding="utf-8").read()
        if args.prompt_file
        else args.prompt
    )
    b64, mime = call_gemini(prompt)
    save_b64(b64, mime, args.out)


CLEAN_PROMPT = (
    "保持整张输入照片的内容和构图完全不变：人物、脸、身体、衣服、动作、体态、"
    "房间、地板、墙面、窗光、阴影和现场物件都不得删除、替换或重绘。"
    "只把整张照片转换为有真实颗粒和自然灰阶的黑白摄影；如画面边缘存在水印，"
    "仅移除水印文字并自然补回该处原背景。不要抠图，不要纯白背景，不要新增任何东西。"
)


def cmd_clean(args):
    in_b64 = image_to_png_b64(args.input)
    b64, mime = call_gemini(CLEAN_PROMPT, in_b64)
    save_b64(b64, mime, args.out)


def main():
    p = argparse.ArgumentParser(prog="gemini_img")
    sub = p.add_subparsers(dest="cmd", required=True)

    g = sub.add_parser("generate", help="生成自然物黑白照片")
    g.add_argument("prompt", help="生成提示词")
    g.add_argument("--prompt-file", action="store_true", help="prompt 参数是文件路径")
    g.add_argument("out", help="输出 PNG 路径")
    g.set_defaults(func=cmd_generate)

    c = sub.add_parser("clean", help="保留原环境，将体式原片转为黑白")
    c.add_argument("input", help="输入体式照片路径")
    c.add_argument("out", help="输出 PNG 路径")
    c.set_defaults(func=cmd_clean)

    args = p.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
