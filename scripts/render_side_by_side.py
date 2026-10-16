"""Compose a strict 50/50 side-by-side yoga/nature diptych.

The 4:3 canvas gives each panel a 2:3 portrait ratio, matching portrait yoga
photographs without shrinking the figure or cropping its long vertical gesture.
"""

import argparse
from pathlib import Path

from PIL import Image, ImageEnhance, ImageOps


W, H = 1440, 1080
PANEL_W = W // 2


def cover(img: Image.Image, size: tuple[int, int], centering=(0.5, 0.5)) -> Image.Image:
    return ImageOps.fit(
        img,
        size,
        method=Image.Resampling.LANCZOS,
        centering=centering,
    )


def open_oriented(path: Path, mode: str) -> Image.Image:
    """Load a copy with orientation metadata applied."""
    with Image.open(path) as source:
        return ImageOps.exif_transpose(source).convert(mode)


def compose(
    nature_path: Path,
    pose_path: Path,
    out_path: Path,
    crop_right: float = 0.0,
    crop_top: float = 0.0,
    crop_bottom: float = 0.0,
    nature_centering_x: float = 0.5,
    nature_centering_y: float = 0.5,
    pose_centering_x: float = 0.5,
    pose_centering_y: float = 0.5,
    nature_contrast: float = 1.03,
    pose_contrast: float = 1.05,
) -> None:
    nature = open_oriented(nature_path, "L")
    pose_rgb = open_oriented(pose_path, "RGB")
    if not 0.0 <= crop_right < 0.5:
        raise ValueError("crop_right must be between 0.0 and 0.5")
    if not 0.0 <= crop_top < 0.5:
        raise ValueError("crop_top must be between 0.0 and 0.5")
    if not 0.0 <= crop_bottom < 0.5:
        raise ValueError("crop_bottom must be between 0.0 and 0.5")
    if crop_top + crop_bottom >= 0.8:
        raise ValueError("combined top and bottom crop must be below 0.8")
    if not 0.0 <= nature_centering_x <= 1.0:
        raise ValueError("nature_centering_x must be between 0.0 and 1.0")
    if not 0.0 <= nature_centering_y <= 1.0:
        raise ValueError("nature_centering_y must be between 0.0 and 1.0")
    if not 0.0 <= pose_centering_x <= 1.0:
        raise ValueError("pose_centering_x must be between 0.0 and 1.0")
    if not 0.0 <= pose_centering_y <= 1.0:
        raise ValueError("pose_centering_y must be between 0.0 and 1.0")
    if nature_contrast <= 0 or pose_contrast <= 0:
        raise ValueError("contrast values must be positive")
    if crop_right:
        clean_width = max(1, int(pose_rgb.width * (1.0 - crop_right)))
        pose_rgb = pose_rgb.crop((0, 0, clean_width, pose_rgb.height))
    if crop_top:
        clean_top = min(pose_rgb.height - 1, int(pose_rgb.height * crop_top))
        pose_rgb = pose_rgb.crop((0, clean_top, pose_rgb.width, pose_rgb.height))
    if crop_bottom:
        clean_bottom = max(1, int(pose_rgb.height * (1.0 - crop_bottom)))
        pose_rgb = pose_rgb.crop((0, 0, pose_rgb.width, clean_bottom))
    pose = pose_rgb.convert("L")

    nature_panel = cover(
        nature,
        (PANEL_W, H),
        centering=(nature_centering_x, nature_centering_y),
    )
    nature_panel = ImageEnhance.Contrast(nature_panel).enhance(nature_contrast)

    pose_panel = cover(
        pose,
        (PANEL_W, H),
        centering=(pose_centering_x, pose_centering_y),
    )
    pose_panel = ImageEnhance.Contrast(pose_panel).enhance(pose_contrast)

    canvas = Image.new("L", (W, H))
    # Series rule: person is always on the left, nature is always on the right.
    canvas.paste(pose_panel, (0, 0))
    canvas.paste(nature_panel, (PANEL_W, 0))
    out_path.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(out_path, "PNG")
    print(f"已合成左右 50/50 版本: {out_path} ({W}x{H})")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("nature", type=Path)
    parser.add_argument("pose", type=Path)
    parser.add_argument("out", type=Path)
    parser.add_argument(
        "--crop-right",
        type=float,
        default=0.0,
        help="Fraction of the pose image to crop from the right before layout.",
    )
    parser.add_argument(
        "--crop-top",
        type=float,
        default=0.0,
        help="Fraction of the pose image to crop from the top before layout.",
    )
    parser.add_argument(
        "--crop-bottom",
        type=float,
        default=0.0,
        help="Fraction of the pose image to crop from the bottom before layout.",
    )
    parser.add_argument("--nature-centering-x", type=float, default=0.5)
    parser.add_argument("--nature-centering-y", type=float, default=0.5)
    parser.add_argument("--pose-centering-x", type=float, default=0.5)
    parser.add_argument("--pose-centering-y", type=float, default=0.5)
    parser.add_argument("--nature-contrast", type=float, default=1.03)
    parser.add_argument("--pose-contrast", type=float, default=1.05)
    args = parser.parse_args()
    compose(
        args.nature,
        args.pose,
        args.out,
        crop_right=args.crop_right,
        crop_top=args.crop_top,
        crop_bottom=args.crop_bottom,
        nature_centering_x=args.nature_centering_x,
        nature_centering_y=args.nature_centering_y,
        pose_centering_x=args.pose_centering_x,
        pose_centering_y=args.pose_centering_y,
        nature_contrast=args.nature_contrast,
        pose_contrast=args.pose_contrast,
    )


if __name__ == "__main__":
    main()
