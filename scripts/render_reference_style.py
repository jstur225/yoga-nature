"""Compose a strict 50/50 top-bottom yoga/nature diptych on a 3:4 canvas.

The 3:4 canvas gives each panel a 3:2 landscape ratio, allowing horizontal,
arched, and compact poses to fill the frame without excessive vertical scene.
"""

import argparse
from pathlib import Path

from PIL import Image, ImageEnhance, ImageOps


DEFAULT_W, DEFAULT_H = 1080, 1440


def cover(
    img: Image.Image,
    size: tuple[int, int],
    centering: tuple[float, float] = (0.5, 0.5),
) -> Image.Image:
    """Resize and center-crop an image so it fills size."""
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
    crop_top: float = 0.0,
    crop_right: float = 0.0,
    crop_bottom: float = 0.0,
    width: int = DEFAULT_W,
    height: int = DEFAULT_H,
    nature_centering: tuple[float, float] = (0.5, 0.5),
    pose_centering: tuple[float, float] = (0.5, 0.5),
    nature_contrast: float = 1.03,
    pose_contrast: float = 1.05,
) -> None:
    if width <= 0 or height <= 0 or height % 2:
        raise ValueError("width and height must be positive; height must be even")
    nature = open_oriented(nature_path, "L")
    pose = open_oriented(pose_path, "L")

    for name, value in (
        ("crop_top", crop_top),
        ("crop_right", crop_right),
        ("crop_bottom", crop_bottom),
    ):
        if not 0.0 <= value < 0.5:
            raise ValueError(f"{name} must be between 0.0 and 0.5")
    if crop_top + crop_bottom >= 0.8:
        raise ValueError("crop_top + crop_bottom must be less than 0.8")
    if nature_contrast <= 0 or pose_contrast <= 0:
        raise ValueError("contrast values must be positive")
    if crop_top or crop_right or crop_bottom:
        clean_width = max(1, int(pose.width * (1.0 - crop_right)))
        clean_top = int(pose.height * crop_top)
        clean_bottom = max(clean_top + 1, int(pose.height * (1.0 - crop_bottom)))
        pose = pose.crop((0, clean_top, clean_width, clean_bottom))

    panel_h = height // 2
    nature = cover(nature, (width, panel_h), centering=nature_centering)
    nature = ImageEnhance.Contrast(nature).enhance(nature_contrast)
    pose_panel = cover(pose, (width, panel_h), centering=pose_centering)
    pose_panel = ImageEnhance.Contrast(pose_panel).enhance(pose_contrast)

    canvas = Image.new("L", (width, height))
    canvas.paste(nature, (0, 0))
    canvas.paste(pose_panel, (0, panel_h))
    out_path.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(out_path, "PNG")
    print(f"已合成上下 50/50 版本: {out_path} ({width}x{height})")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("nature", type=Path)
    parser.add_argument("pose", type=Path)
    parser.add_argument("out", type=Path)
    parser.add_argument(
        "--crop-top",
        type=float,
        default=0.0,
        help="Fraction of the pose image to crop from the top before layout.",
    )
    parser.add_argument(
        "--crop-right",
        type=float,
        default=0.0,
        help="Fraction of the pose image to crop from the right before layout.",
    )
    parser.add_argument(
        "--crop-bottom",
        type=float,
        default=0.0,
        help="Fraction of the pose image to crop from the bottom before layout.",
    )
    parser.add_argument("--width", type=int, default=DEFAULT_W)
    parser.add_argument("--height", type=int, default=DEFAULT_H)
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
        crop_top=args.crop_top,
        crop_right=args.crop_right,
        crop_bottom=args.crop_bottom,
        width=args.width,
        height=args.height,
        nature_centering=(args.nature_centering_x, args.nature_centering_y),
        pose_centering=(args.pose_centering_x, args.pose_centering_y),
        nature_contrast=args.nature_contrast,
        pose_contrast=args.pose_contrast,
    )


if __name__ == "__main__":
    main()
