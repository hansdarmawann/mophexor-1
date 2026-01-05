import pywintypes
import win32file
from pathlib import Path


def sync_timestamps(src: Path, dst: Path):
    s = src.stat()

    handle = win32file.CreateFile(
        str(dst),
        win32file.GENERIC_WRITE,
        0,
        None,
        win32file.OPEN_EXISTING,
        win32file.FILE_ATTRIBUTE_NORMAL,
        None,
    )

    win32file.SetFileTime(
        handle,
        pywintypes.Time(s.st_ctime),
        pywintypes.Time(s.st_atime),
        pywintypes.Time(s.st_mtime),
    )

    handle.close()
