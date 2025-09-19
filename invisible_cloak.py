import cv2
import numpy as np
import time

print("""
Harry :  Hey !! Would you like to try my invisibility cloak ??
         It's awesome !!

         Prepare to get invisible .....................
""")

# Open webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Error reading from webcam.")
    exit()

# ---------------- Step 1: Capture Background ----------------
print("📸 Capturing background... Make sure NO person is in front of the camera!")

time.sleep(2)  # warm-up camera
background = None
for i in range(50):  # capture multiple frames for stable background
    ret, frame = cap.read()
    if not ret:
        continue
    frame = cv2.flip(frame, 1)  # flip for mirror view
    background = frame.copy()

print("✅ Background captured successfully!")

# ---------------- Step 2: Start Cloak Effect ----------------
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)  # flip for natural look

    # Convert current frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define red color range (cloak color)
    lower_red1 = np.array([0, 120, 70])
    upper_red1 = np.array([10, 255, 255])
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)

    lower_red2 = np.array([170, 120, 70])
    upper_red2 = np.array([180, 255, 255])
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)

    # Combine masks
    mask = mask1 + mask2

    # Clean mask using morphological operations
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
    mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, np.ones((3, 3), np.uint8))

    # Apply the mask to background
    part1 = cv2.bitwise_and(background, background, mask=mask)

    # Invert mask and apply to original frame
    mask_inv = cv2.bitwise_not(mask)
    part2 = cv2.bitwise_and(frame, frame, mask=mask_inv)

    # Combine both results
    final_output = cv2.addWeighted(part1 + part2, 1, part1 + part2, 0, 0)

    cv2.imshow("🧙‍♂️ Invisibility Cloak (Red)", final_output)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
