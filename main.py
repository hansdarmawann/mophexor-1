from pathlib import Path
from config import (
    ROOT_DIR,
    EXIFTOOL_PATH,
    MIN_MP4_SIZE,
    IMAGE_EXTENSIONS,
)
from extractor import process_image


def main():
    for file in ROOT_DIR.rglob("*"):
        if file.suffix.lower() in IMAGE_EXTENSIONS:
            try:
                process_image(file, EXIFTOOL_PATH, MIN_MP4_SIZE)
            except Exception as e:
                print(f"[ERROR] {file}: {e}")


if __name__ == "__main__":
    main()
