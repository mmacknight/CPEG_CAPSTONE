import cv2
import numpy as np
import time

# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
def applyCustomColorMap(im_gray) :

    lut = np.zeros((256, 1, 3), dtype=np.uint8)

    lut[:, 0, 0] = [i for i in range(150)] + [0 for i in range(106)]

    lut[:, 0, 1] = [i for i in range(150)] + [0 for i in range(106)]

    lut[:, 0, 2] = [i for i in range(150)] + [0 for i in range(106)]


    im_color = cv2.LUT(im_gray, lut)

    return im_color;

cap = cv2.VideoCapture(0)

# Check if camera opened successfully
if (cap.isOpened()== False):
  print("Error opening video stream or file")

# Read until video is completed
while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()
  if ret == True:

    # Display the resulting frame
    im_color = applyCustomColorMap(frame);
    # im_color = cv2.applyColorMap(frame, cv2.COLORMAP_JET)
    # for r1 in im_color:
    #     for r2 in r1:
    #         for color in r2:
    #             if color:
    #                 print(r2,color)
    # time.sleep(1000000);
    cv2.imshow('Frame',im_color)
    # Press Q on keyboard to  exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break

  # Break the loop
  else:
    break

# When everything done, release the video capture object
cap.release()

# Closes all the frames
cv2.destroyAllWindows()
