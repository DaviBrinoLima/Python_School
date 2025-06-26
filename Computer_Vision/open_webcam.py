import cv2 as cv

capture = cv.VideoCapture(0)

while True:
    status, frame = capture.read()

    if (not status) or (cv.waitKey(1) == ord("q")):
        capture.release()
        cv.destroyAllWindows
        break

    cv.imshow("WebCam", frame)

