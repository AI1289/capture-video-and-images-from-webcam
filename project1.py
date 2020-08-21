                                    #extracting embeddings part starts from here
# import the necessary packages
from sklearn.preprocessing import LabelEncoder
import sklearn.svm
from imutils import paths
import numpy as np
import imutils
import pickle
import cv2
import os
import sklearn


the_file_name = input("enter file name: ")
the_path = "/home/abhi/Desktop/opencv-face-recognition-extended/opencv-face-recognition/dataset/{}".format(the_file_name)
os.mkdir(the_path)
output_video_path = "/home/abhi/Desktop/opencv-face-recognition-extended/opencv-face-recognition/dataset/{}/video.avi".format(the_file_name)
capture = cv2.VideoCapture(0)

# Get some properties of VideoCapture (frame width, frame height and frames per second (fps)):
frame_width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
frame_height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = capture.get(cv2.CAP_PROP_FPS)

# Print these values:
print("CV_CAP_PROP_FRAME_WIDTH: '{}'".format(frame_width))
print("CV_CAP_PROP_FRAME_HEIGHT : '{}'".format(frame_height))
print("CAP_PROP_FPS : '{}'".format(fps))

# FourCC is a 4-byte code used to specify the video codec and it is platform dependent!
# In this case, define the codec XVID
# This line also works:
# fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
fourcc = cv2.VideoWriter_fourcc(*'XVID')

# Create VideoWriter object. We use the same properties as the input camera.
# Last argument is False to write the video in grayscale. True otherwise (write the video in color)
out_gray = cv2.VideoWriter(output_video_path, fourcc, int(fps), (int(frame_width), int(frame_height)), True)

# Read until video is completed or 'q' is pressed
while capture.isOpened():
    # Read the frame from the camera
    ret, frame = capture.read()
    if ret is True:

        # Convert the frame to grayscale
      #  gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Write the grayscale frame to the video
        out_gray.write(frame)
        cv2.imshow('color', frame)
        # We show the frame (this is not necessary to write the video)
        # But we show it until 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
# Release everything:
capture.release()
out_gray.release()
cv2.destroyAllWindows()
# Create a VideoCapture object.
video_path = "/home/abhi/Desktop/opencv-face-recognition-extended/opencv-face-recognition/dataset/{}/video.avi".format(the_file_name)
capture = cv2.VideoCapture(video_path)

# Check if the video is opened successfully
if capture.isOpened() is False:
    print("Error opening the video file!")
frame_index = 0
the_index = 0
while capture.isOpened():
    # Capture frame-by-frame from the video file
    ret, frame = capture.read()

    if ret is True:

        if frame_index <= 500:
            frame_name = "/home/abhi/Desktop/opencv-face-recognition-extended/opencv-face-recognition/dataset/{}/".format(the_file_name)
            frame_name2 = frame_name + "{}.png".format(the_index)
            cv2.imwrite(frame_name2, frame)
            frame_index += 5
            the_index += 1


    # Press q on keyboard to exit the program
        if the_index == 100:
            break
    # Break the loop
    else:
        break

# Release everything
capture.release()
cv2.destroyAllWindows()
