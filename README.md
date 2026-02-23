# Face Anonymizer

Real-time face detection and anonymization in videos, built with **MediaPipe** and **OpenCV**.

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-4.13-5C3EE8?logo=opencv&logoColor=white)
![MediaPipe](https://img.shields.io/badge/MediaPipe-0.10.8-FF6F00?logo=google&logoColor=white)
![License: MIT](https://img.shields.io/badge/License-MIT-green)

---

## Overview

This tool processes video files (or webcam feeds), detects faces frame-by-frame using Google's MediaPipe, and applies an anonymization effect over each detected face. It supports three different methods: Gaussian blur, pixelation, and black-out masking.

Each detection is displayed with a bounding box and its confidence score.

## Project Structure

```
Face Anonymizer/
├── main.py              # Entry point — video loop, detection, rendering
├── utils.py             # Helpers — bbox math, anonymization, drawing
├── requirements.txt     # Python dependencies
├── Test Data/
│   └── test video.mp4   # Sample test video
├── LICENSE
└── README.md
```

## How It Works

```
Video Input → Resize (640×480) → MediaPipe Detection → Anonymize Faces → Display
```

1. Frames are captured from the video source and resized to 640×480
2. MediaPipe runs face detection with a configurable confidence threshold (default: `0.6`)
3. Detected face regions are anonymized using the selected method
4. Bounding boxes with confidence labels are drawn on each face
5. Press `ESC` to exit

### Key Functions (`utils.py`)

| Function              | Role                                                                |
| --------------------- | ------------------------------------------------------------------- |
| `get_bbox_pixels()`   | Converts relative bounding box to pixel coordinates (with clamping) |
| `anonymize_face()`    | Applies blur, pixelation, or black-out to a face region             |
| `draw_bounding_box()` | Draws the detection rectangle and confidence score                  |

## Getting Started

### Prerequisites

- Python 3.8 or higher

### Installation

```bash
git clone https://github.com/your-username/face-anonymizer.git
cd face-anonymizer

# Create virtual environment (recommended)
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # macOS / Linux

pip install -r requirements.txt
```

### Run

```bash
python main.py
```

## Configuration

All config is in `main.py` — no CLI args needed, just edit the values directly:

**Video source:**
```python
video_path = './Test Data/test video.mp4'
# video_path = 0   # use webcam instead
```

**Anonymization method** — `"blur"` | `"pixelate"` | `"black"`:
```python
frame = anonymize_face(frame, xmin, ymin, xmax, ymax, method="blur")
```

**Detection sensitivity** — lower values catch more faces, higher values are stricter:
```python
min_detection_confidence=0.6
```

## Anonymization Methods

| Method     | Description                              |
| ---------- | ---------------------------------------- |
| `blur`     | Gaussian blur with a 51×51 kernel        |
| `pixelate` | Downscale to 16×16 px, then upscale back |
| `black`    | Solid black fill over the face region    |

## Dependencies

| Package         | Version          | Role                        |
| --------------- | ---------------- | --------------------------- |
| `opencv-python` | 4.13.0.92        | Video I/O, image processing |
| `mediapipe`     | 0.10.8           | Face detection model        |
| `numpy`         | _auto-installed_ | Array operations            |

## Contributing

If you'd like to contribute, feel free to open an issue or submit a PR. Some ideas:

- CLI interface with `argparse`
- Save anonymized video to file
- Additional anonymization styles (emoji overlay, mosaic, etc.)
- Multi-face tracking for smoother output

## License

This project is licensed under the MIT License — see [LICENSE](LICENSE) for details.
