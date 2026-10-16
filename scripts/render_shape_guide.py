"""Render a non-identifying geometry guide from normalized JSON strokes."""

import argparse
import json
from pathlib import Path

from PIL import Image, ImageDraw


SCALE = 3


def px(point, width, height):
    x, y = point
    return round(float(x) * width), round(float(y) * height)


def render(signature_path: Path, output_path: Path) -> None:
    data = json.loads(signature_path.read_text(encoding="utf-8"))
    canvas = data.get("canvas", {})
    width = int(canvas.get("width", 1024))
    height = int(canvas.get("height", 1536))
    if width <= 0 or height <= 0:
        raise ValueError("canvas width and height must be positive")

    large = Image.new("L", (width * SCALE, height * SCALE), 255)
    draw = ImageDraw.Draw(large)

    for shape in data.get("closed_shapes", []):
        points = [px(p, width * SCALE, height * SCALE) for p in shape["points"]]
        if len(points) >= 3:
            draw.polygon(points, outline=0, fill=None, width=max(3, int(shape.get("weight", 12)) * SCALE))

    for stroke in data.get("strokes", []):
        points = [px(p, width * SCALE, height * SCALE) for p in stroke["points"]]
        if len(points) >= 2:
            draw.line(
                points,
                fill=0,
                width=max(3, int(stroke.get("weight", 16)) * SCALE),
                joint="curve",
            )

    for node in data.get("nodes", []):
        x, y = px(node["point"], width * SCALE, height * SCALE)
        radius = max(5, int(node.get("radius", 12)) * SCALE)
        draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=0)

    guide = large.resize((width, height), Image.Resampling.LANCZOS)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    guide.save(output_path, "PNG")
    print(f"已生成形态引导图: {output_path} ({width}x{height})")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("signature", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    render(args.signature, args.output)


if __name__ == "__main__":
    main()
