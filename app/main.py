import cv2

import settings
import opencv_utils


capture = cv2.VideoCapture(settings.WEBCAM_URL)

while True:
    success, image = capture.read()

    # Show image results
    image_stack = opencv_utils.stack_images(1, ([image]))
    cv2.imshow("Press 'Q' to exit", image_stack)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
