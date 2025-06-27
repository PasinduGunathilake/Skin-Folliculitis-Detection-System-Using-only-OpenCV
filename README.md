# Skin Folliculitis Detection using OpenCV

This project detects folliculitis in images by processing skin images with OpenCV. It uses contour detection on thresholded grayscale images to count folliculitis spots and annotate them on the image.

---

## Overview

- Reads an image of skin.
- Converts the image from BGR to RGB and then to HSV color space.
- Converts the HSV image to grayscale.
- Applies binary thresholding to detect features.
- Finds contours on the thresholded image.
- Filters contours by area to identify folliculitis.
- Draws bounding boxes and labels the detected folliculitis on the original image.
- Displays processed images with annotations.

---

## Files

- `si.jpg` — Sample skin image (place inside `src/` folder).
- `detect_folliculitis.py` — Script performing image processing and folliculitis detection.

---

## Requirements

- Python 3.x
- OpenCV (`opencv-python`)
- matplotlib

Install dependencies with:

```bash
pip install opencv-python matplotlib
