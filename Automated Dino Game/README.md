# Auto [Dino Game](https://poki.com/en/g/dinosaur-game) Player

This project implements an automated player for the popular offline Dinosaur game found in Google Chrome's offline mode. The player utilizes computer vision techniques to detect obstacles and trigger jumps accordingly.

With the initial sampling of : [Link](https://www.youtube.com/watch?v=R95coF8wF1o)

## Features

- **Screen Capture**: Utilizes MSS library to capture a specific region of the screen where the game is located.
- **Image Pre-processing**: Converts the captured image to grayscale, applies thresholding, and edge detection to prepare it for obstacle detection.
- **Obstacle Detection**: Identifies obstacles (cacti) using contour detection techniques.
- **Game Logic**: Determines when to trigger jumps based on the proximity of the next obstacle.
- **FPS Monitoring**: Displays the frames per second (FPS) to monitor the performance of the player.
- **User Interaction**: Pressing 'q' quits the game loop.

## Requirements

- Python 3.x
- OpenCV
- NumPy
- PyAutoGUI
- MSS
- cvzone

## Installation

1. Clone the repository:

```bash
git clone https://github.com/awrsha/Automated-Dino-Game.git
```

2. Install the required Python packages:

```bash
pip install opencv-python
pip install numpy
pip install pyautogui
pip install mss
pip install cvzone
```

## Usage

1. Run the `Automated Dino Game.py` script:

```bash
python Automated Dino Game.py
```

2. Open the offline Dinosaur game in Google Chrome.
3. Adjust the screen region parameters in `Automated Dino Game.py` to match the game's location on your screen if needed.
4. Watch the automated player in action!

## License

- see the [LICENSE](LICENSE) file for details.
