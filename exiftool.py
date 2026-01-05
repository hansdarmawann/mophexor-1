import subprocess
from pathlib import Path


def has_motion_photo(exiftool: Path, image: Path) -> bool:
    result = subprocess.run(
        [str(exiftool), "-s", "-s", "-s", "-MotionPhotoVideo", str(image)],
        capture_output=True,
        text=True
    )
    return bool(result.stdout.strip())


def extract_motion_video(exiftool: Path, image: Path, suffix="_motion.mp4"):
    subprocess.run(
        [
            str(exiftool),
            "-b",
            "-MotionPhotoVideo",
            "-w",
            suffix,
            str(image)
        ],
        check=False
    )
