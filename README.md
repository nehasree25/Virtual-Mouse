# Virtual Mouse Using MediaPipe Hand Tracking

## Overview

This project implements a virtual mouse using hand gestures detected through a webcam. It uses MediaPipe's hand landmark detection to track the user's hand and control the mouse cursor on the screen.

The index finger is used to move the cursor, while bringing the thumb close to the index finger performs a mouse click.

---

## Features

* Real-time hand tracking using MediaPipe
* Cursor movement using index finger
* Mouse click gesture using thumb and index finger
* Webcam-based interaction
* Landmark visualization on the video feed

---

## Technologies Used

* Python
* OpenCV
* MediaPipe
* PyAutoGUI

---

## Project Structure

```
project/
│
├── main.py
├── handDetector.py
├── README.md
```

### main.py

* Captures video from the webcam.
* Detects hand landmarks.
* Displays the processed video feed.

### handDetector.py

* Implements the `HandDetector` class.
* Detects hand landmarks using MediaPipe.
* Controls mouse movement and click actions.

---

## Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd virtual-mouse
```

### 2. Install Dependencies

```bash
pip install opencv-python mediapipe pyautogui
```

---

## How It Works

### Cursor Movement

The position of the index finger tip (Landmark 8) is mapped to the screen coordinates.

```python
pg.moveTo(index_width, index_height)
```

### Mouse Click

When the thumb tip (Landmark 4) comes close to the index finger tip, a click event is triggered.

```python
if abs(thumb_height - self.index_height) < 20:
    pg.click()
```

---

## Hand Landmarks Used

| Landmark ID | Finger Point     |
| ----------- | ---------------- |
| 4           | Thumb Tip        |
| 8           | Index Finger Tip |

---

## Running the Project

Execute:

```bash
python main.py
```

Press **ESC** to exit the application.

---

## Future Improvements

* Smooth cursor movement
* Left and right click gestures
* Drag and drop functionality
* Scroll gesture support
* Gesture-based keyboard shortcuts
* Multi-hand support

---

## Output

* Hand landmarks are displayed on the webcam feed.
* Moving the index finger controls the mouse cursor.
* Bringing the thumb close to the index finger performs a click.


