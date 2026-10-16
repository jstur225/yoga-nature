"""Check local runtime requirements without installing or changing anything."""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path


MIN_PYTHON = (3, 10)
MAX_PYTHON = (3, 14)
MIN_PILLOW_MAJOR = 10
MAX_PILLOW_MAJOR = 12


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--workdir", type=Path, required=True)
    args = parser.parse_args()

    errors: list[str] = []
    result: dict[str, object] = {
        "status": "ok",
        "python": ".".join(map(str, sys.version_info[:3])),
        "input": str(args.input),
        "workdir": str(args.workdir),
    }

    if sys.version_info < MIN_PYTHON:
        errors.append("Python 3.10 or newer is required")
    elif sys.version_info[:2] > MAX_PYTHON:
        errors.append("Python versions newer than 3.14 have not been validated")

    pillow = None
    image_module = None
    try:
        import PIL
        from PIL import Image

        pillow = PIL.__version__
        image_module = Image
        pillow_major = int(pillow.split(".", 1)[0])
        if not MIN_PILLOW_MAJOR <= pillow_major <= MAX_PILLOW_MAJOR:
            errors.append("Pillow 10.x through 12.x is required")
    except (ImportError, ValueError):
        errors.append("Pillow is not installed or its version cannot be parsed")
    result["pillow"] = pillow

    if not args.input.is_file():
        errors.append("The selected input image does not exist or is not a file")
    elif image_module is not None:
        try:
            with image_module.open(args.input) as image:
                image.verify()
        except Exception as exc:  # Pillow provides format-specific exception types.
            errors.append(f"The selected input cannot be decoded as an image: {exc}")

    work_parent = args.workdir if args.workdir.exists() else args.workdir.parent
    if not work_parent.exists() or not os.access(work_parent, os.W_OK):
        errors.append("The requested working directory is not writable")

    if errors:
        result["status"] = "blocked"
        result["errors"] = errors

    print("PREFLIGHT_JSON:" + json.dumps(result, ensure_ascii=False))
    return 0 if not errors else 2


if __name__ == "__main__":
    raise SystemExit(main())
