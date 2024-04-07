import cv2
import numpy as np
import pyautogui
from mss import mss
from cvzone.FPS import FPS
import cvzone

# Initialize the FPS reader
fpsReader = FPS()

# Function to capture a screen region using MSS (Multiple Screen Shots)
def capture_screen_region_opencv_mss(x, y, width, height):
    with mss() as sct:
        monitor = {"top": y, "left": x, "width": width, "height": height}
        screenshot = sct.grab(monitor)
        img = np.array(screenshot)
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
        return img

# Pre-processing function to prepare the image for contour detection
def pre_process(img):
    gray_frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, binary_frame = cv2.threshold(gray_frame, 127, 255, cv2.THRESH_BINARY_INV)
    canny_frame = cv2.Canny(binary_frame, 50, 50)
    kernel = np.ones((5, 5))
    dilated_frame = cv2.dilate(canny_frame, kernel, iterations=2)
    return dilated_frame

# Function to find contours (obstacles) in the image
def find_obstacles(imgCrop, imgPre):
    imgContours, conFound = cvzone.findContours(imgCrop, imgPre, minArea=100, filter=None)
    return imgContours, conFound

# Game logic function to determine when to jump
def game_logic(conFound, imgContours, jump_distance=65):
    if conFound:
        left_most_contour = sorted(conFound, key=lambda x: x["bbox"][0])
        # Draw a line to represent the jump distance
        cv2.line(imgContours, (0, left_most_contour[0]["bbox"][1] + 10),
                 (left_most_contour[0]["bbox"][0], left_most_contour[0]["bbox"][1] + 10), (0, 200, 0), 10)
        # If the leftmost obstacle is close enough, trigger a jump
        if left_most_contour[0]["bbox"][0] < jump_distance:
            pyautogui.press("space")
            print("jump")
    return imgContours

# Main function to run the game loop
def main():
    while True:
        # Capture the game screen region
        imgGame = capture_screen_region_opencv_mss(450, 300, 650, 200)
        # Define the region of interest (ROI) for processing
        cp = 100, 140, 110
        imgCrop = imgGame[cp[0]:cp[1], cp[2]:]
        # Pre-process the cropped image
        imgPre = pre_process(imgCrop)
        # Find obstacles (contours) in the pre-processed image
        imgContours, conFound = find_obstacles(imgCrop, imgPre)
        # Apply game logic to determine when to jump
        imgContours = game_logic(conFound, imgContours)
        # Overlay the processed image onto the original game screen
        imgGame[cp[0]:cp[1], cp[2]:] = imgContours
        # Update FPS and display the game screen
        fps, imgGame = fpsReader.update(imgGame)
        cv2.imshow("Game", imgGame)
        key = cv2.waitKey(1) & 0xFF
        # Exit the game loop if 'q' is pressed
        if key == ord('q'):
            break

    cv2.destroyAllWindows()

# Entry point of the script
if __name__ == "__main__":
    main()
