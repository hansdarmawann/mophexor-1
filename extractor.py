from pathlib import Path
from exiftool import has_motion_photo, extract_motion_video
from timestamps import sync_timestamps


def process_image(image: Path, exiftool: Path, min_mp4_size: int):
    mp4 = image.with_name(image.stem + "_motion.mp4")

    if not has_motion_photo(exiftool, image):
        return

    if mp4.exists():
        if mp4.stat().st_size > min_mp4_size:
            print(f"[SKIP] Already exists: {mp4}")
            return
        else:
            print(f"[REPLACE] Corrupt MP4 (<100KB): {mp4}")
            mp4.unlink()

    extract_motion_video(exiftool, image)

    if mp4.exists():
        sync_timestamps(image, mp4)
        print(f"[OK] Extracted: {mp4}")
