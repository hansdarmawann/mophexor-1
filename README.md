# mophexor: Android Motion Pictures Extractor

`mophexor` is a lightweight Python tool that scans image libraries and extracts
embedded **Motion Photo videos** (`MotionPhotoVideo`) into standalone MP4 files,
while preserving the original file timestamps.

Motion Photos are supported by multiple Android OEMs (e.g. Samsung, Google Pixel,
Xiaomi, Huawei), and this tool works at the **metadata level**, independent of
brand-specific camera apps.

This project is designed as a **local automation utility**, not a PyPI package.

---

## ✨ Features

- Recursively scan folders for `.jpg` and `.heic`
- Detect real Motion Photos via `MotionPhotoVideo` metadata
- Extract embedded video to `*_motion.mp4`
- Skip valid existing MP4 files
- Replace corrupted MP4 files (<100 KB)
- Preserve **creation / modified / access timestamps**
- Windows-native timestamp handling (`pywin32`)
- Brand-agnostic (ExifTool-based)

---

## 🧱 Project Structure

```text
mophexor/
│
├── extractor.py        # Core workflow
├── exiftool.py         # ExifTool wrapper
├── timestamps.py      # Windows timestamp sync
│
├── config.py           # Paths & constants
├── main.py             # Entry point
├── requirements.txt
└── README.md
````

---

## ⚙️ Requirements

* Windows
* Python 3.11
* ExifTool (any modern version; digiKam bundle works)

---

## 🐍 Conda Environment

```bash
conda create -n mophexor python=3.11 pywin32 -y
conda activate mophexor
```

---

## 🚀 Usage

1. Edit `config.py`:

   * `ROOT_DIR`
   * `EXIFTOOL_PATH`

2. Run:

```bash
python main.py
```

---

## 🧠 How It Works

1. Walks the directory tree recursively
2. Checks for the `MotionPhotoVideo` tag using ExifTool
3. Validates existing MP4 outputs
4. Extracts the embedded video stream if needed
5. Syncs timestamps from the source image

---

## ⚠️ Notes & Limitations

* Requires ExifTool installed locally
* Timestamp syncing is Windows-specific
* Works on metadata only (no image decoding)
* Behavior depends on OEM metadata compliance