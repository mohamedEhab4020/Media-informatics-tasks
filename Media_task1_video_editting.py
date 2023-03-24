import cv2

import numpy as np


# Function to rotate image by 90 degrees counter clockwise
def rotate(cap):
    while True:

        s,new_image = cap.read()
        new_image =  cv2.rotate(new_image, cv2.ROTATE_90_COUNTERCLOCKWISE)
        cv2.imshow("Transformed frame",new_image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            return


# Function to shear image in the X axis
def shear(cap):

    while True:

        s,new_image = cap.read()
        rows, cols = new_image.shape[:2]
        M = np.float32([[1, 0.5, 0], [0, 1, 0], [0, 0, 1]])
        new_image = cv2.warpPerspective(new_image, M, (cols, rows))
        cv2.imshow("Transformed frame",new_image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            return




# Function to reflect image on the Y-axis
def reflect(cap):
    while True:

        s,new_image = cap.read()
        new_image = cv2.flip(new_image, 1)
        cv2.imshow("Transformed frame",new_image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            return



# required operations
def perform_func(pressed_key, cap):
    if pressed_key == ord('r'):
        return rotate(cap)
    elif pressed_key == ord('h'):
        return shear(cap)
    elif pressed_key == ord('l'):
        return reflect(cap)


cap = cv2.VideoCapture(0)  # Capture video from default camera

while True:
    # Read frame from video
    is_working, img = cap.read()
    if not is_working:
        break

    # Check if keys are pressed to apply transformations
    cv2.imshow("Frame", img)
    pressed_key = cv2.waitKey(1) & 0xFF
    img = perform_func(pressed_key, cap)

    # Display the transformed frame
    if img is not None and img.shape[0] > 0 and img.shape[1] > 0:
        cv2.imshow("TransformedFrame", img)


    # Check if 'q' is pressed to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()  # Release the camera resource
cv2.destroyAllWindows()  # destroy all windows