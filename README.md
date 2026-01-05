# mophexor — Motion Photo Extractor

`mophexor` is a lightweight Python utility for extracting embedded **Motion Photo
video streams** (`MotionPhotoVideo`) from image files into standalone MP4 files,
while preserving original file timestamps.

The tool operates purely at the **metadata level** using ExifTool and is
**OEM-agnostic**, supporting Motion Photos produced by multiple Android devices
(e.g. Samsung, Google Pixel, Xiaomi, Huawei).

This project is designed as a **local automation and data-ingestion utility**,
not as a PyPI-distributed package.

> ⚠️ **Platform note:**  
> `mophexor` is **currently available only on Windows**, due to its use of
> Windows-native file timestamp APIs.

---

## ✨ Features

- Recursive scan of image folders
- Supports `.jpg` and `.heic`
- Detects Motion Photos via `MotionPhotoVideo` metadata
- Extracts embedded video to `*_motion.mp4`
- Skips valid existing MP4 files
- Replaces corrupted MP4 files (<100 KB)
- Preserves creation / modified / access timestamps
- Windows-native timestamp handling
- Deterministic and re-runnable

---

## 🧱 Project Structure

Based on the current repository layout:

```text
mophexor/
│
├── config.py              # Configuration (paths, thresholds)
├── main.py                # Entry point
│
├── extractor.py           # Core extraction workflow
├── exiftool.py            # ExifTool subprocess wrapper
├── timestamps.py          # Windows timestamp synchronization
│
├── exiftool-13.45_64/     # Bundled ExifTool binary (third-party)
│   └── exiftool(-k).exe
│
├── sample/                # Sample input images
├── NOTICE                 # Third-party attributions
├── README.md
└── requirements.txt
````

---

## ⚙️ Requirements

* **Windows (required)**
* Python 3.11
* ExifTool (bundled or external)

---

## 🐍 Conda Environment

```bash
conda create -n mophexor python=3.11 pywin32 -y
conda activate mophexor
```

---

## 🚀 Usage

1. Edit `config.py`:

   * Set `ROOT_DIR` to the folder containing images
   * Set `EXIFTOOL_PATH` to `exiftool(-k).exe`

2. Run:

```bash
python main.py
```

---

## 🧠 How It Works

1. Walks the directory tree recursively
2. Checks for the `MotionPhotoVideo` tag using ExifTool
3. Validates existing MP4 outputs
4. Extracts embedded video streams when needed
5. Synchronizes timestamps from source image to MP4

---

## 🔐 Third-Party Software

This project relies on **ExifTool**, developed by **Phil Harvey**, for reading and
extracting Motion Photo metadata.

ExifTool is **free and open-source software**, licensed under the **Perl Artistic
License**, which permits use, redistribution, and bundling.

Attribution and license details for ExifTool are provided in the
[`NOTICE`](./NOTICE) file.

`mophexor` does **not** modify ExifTool and does **not** claim ownership over it.

---

## ⚠️ Notes & Limitations

* **Windows-only (for now)**
* Timestamp synchronization is Windows-specific
* Works on metadata only (no image decoding)
* Behavior depends on OEM metadata compliance
* Intended for local / personal / internal automation

---

## 📜 License

This project is provided for personal and internal use.