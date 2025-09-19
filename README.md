# 🧙‍♂️ Invisibility Cloak Using OpenCV

A fun Python project that makes a red cloak "invisible" using **OpenCV** and **NumPy**. The program replaces the red color cloak with the background captured from the webcam, creating a magical invisibility effect—just like Harry Potter! 🪄

---

## **Demo**

![Invisibility Cloak Demo](demo.gif)  
*(Replace with your own GIF or screenshots)*

---

## **Features**

- Captures a static background when no person is in front of the camera.
- Detects red color (or cloak) in real-time using HSV color space.
- Makes the cloak appear invisible by replacing it with the background.
- Real-time webcam processing with live output.
- Easy to extend for other colors.

---

## **Requirements**

- Python 3.x
- OpenCV (`cv2`)
- NumPy (`numpy`)

Install dependencies with:

```bash
pip install opencv-python numpy
