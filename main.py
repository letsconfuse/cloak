import numpy as np
import cv2
import time

# Initialize webcam
cap = cv2.VideoCapture(0)
time.sleep(2)  # Allow camera to adjust

# Capture the background frame
background_frames = []
for _ in range(30):  # Capture multiple frames for stability
    ret, frame = cap.read()
    if ret:
        frame = np.flip(frame, axis=1)  # Flip for correct orientation
        background_frames.append(frame)

if len(background_frames) == 0:
    print("Error: Couldn't capture background")
    cap.release()
    exit()

# Compute the median background (to avoid flickering)
background = np.median(background_frames, axis=0).astype(np.uint8)

print("Background captured successfully. Starting cloak effect...")

## **Main Loop: Detect and Replace Black Color**
while cap.isOpened():
    ret, img = cap.read()
    if not ret:
        break

    img = np.flip(img, axis=1)  # Mirror the frame

    # Convert to HSV color space
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Define black color range in HSV
    lower_black = np.array([0, 0, 0])
    upper_black = np.array([180, 255, 50])  # Adjust brightness threshold for better detection

    # Create mask to detect black color
    mask = cv2.inRange(hsv, lower_black, upper_black)

    # Apply noise reduction
    mask = cv2.GaussianBlur(mask, (5, 5), 0)
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, kernel)

    # Extract background where black color is detected
    cloaked_part = cv2.bitwise_and(background, background, mask=mask)

    # Invert mask to keep non-black regions
    mask_inv = cv2.bitwise_not(mask)
    foreground = cv2.bitwise_and(img, img, mask=mask_inv)

    # Merge background and foreground
    final_output = cv2.addWeighted(cloaked_part, 1, foreground, 1, 0)

    # Display the result
    cv2.imshow("Harry Potter's Black Invisible Cloak", final_output)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
