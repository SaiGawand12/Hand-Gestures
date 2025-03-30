# Hand Gesture Tracking with OpenCV & Mediapipe

This project implements hand gesture tracking using OpenCV and Mediapipe to perform basic actions based on the number of detected fingers. The actions include zooming, applying filters, and resetting the view.

## Features
- **Hand tracking** using Mediapipe
- **Gesture-based effects:**
  - 1 finger: Zoom out
  - 2 fingers: Grayscale filter
  - 3 fingers: Blur effect
  - 4 fingers: Color inversion
  - 5 fingers: Reset view
  - No fingers: No action (idle state)

## Requirements
Make sure you have Python installed and the following dependencies:

```bash
pip install opencv-python mediapipe numpy
```

## Usage
Run the script to start gesture tracking:

```bash
python hand_gesture_tracking.py
```

## How It Works
- The script uses **Mediapipe Hands** to detect hand landmarks in real time.
- The number of extended fingers is counted and mapped to specific actions.
- OpenCV applies effects like zooming, grayscale, blurring, and color inversion based on gestures.
- The program runs on a webcam feed and updates continuously.

## Controls
- **Show one finger** → Zoom out
- **Show two fingers** → Apply grayscale filter
- **Show three fingers** → Apply blur effect
- **Show four fingers** → Invert colors
- **Show five fingers** → Reset the view
- **No fingers** → No action
- **Press 'Q'** → Quit the program


## Contribution
Feel free to fork this repository, improve the code, and submit pull requests!

## License
This project is open-source and available under the MIT License.

---
Happy coding! 🎯🚀