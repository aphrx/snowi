import numpy as np
import cv2
import RPi.GPIO as GPIO

cap = cv2.VideoCapture(0)

# video recorder
fourcc = cv2.CV_FOURCC(*'XVID')  # cv2.VideoWriter_fourcc() does not exist
video_writer = cv2.VideoWriter("output.avi", fourcc, 20, (680, 480))

in1 = 27
in2 = 22
in3 = 24
in4 = 25

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret:
        video_writer.write(frame)
        cv2.imshow('Video Stream', frame)

    # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.LOW)
        GPIO.output(in3, GPIO.LOW)
        GPIO.output(in4, GPIO.LOW)
        break

    key = cv2.waitKey(1) & 0xFF
    # Forward
    if key == ord('w'):
        GPIO.output(in1, GPIO.HIGH)
        GPIO.output(in2, GPIO.LOW)
        GPIO.output(in3, GPIO.HIGH)
        GPIO.output(in4, GPIO.LOW)

    # Right
    if key == ord('d'):
        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.LOW)
        GPIO.output(in3, GPIO.HIGH)
        GPIO.output(in4, GPIO.LOW)

    # Back
    if key == ord('s'):
        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.HIGH)
        GPIO.output(in3, GPIO.LOW)
        GPIO.output(in4, GPIO.HIGH)

    # Left
    if key == ord('a'):
        GPIO.output(in1, GPIO.HIGH)
        GPIO.output(in2, GPIO.LOW)
        GPIO.output(in3, GPIO.LOW)
        GPIO.output(in4, GPIO.LOW)

    if key == ord('e'):
        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.LOW)
        GPIO.output(in3, GPIO.LOW)
        GPIO.output(in4, GPIO.LOW)

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

