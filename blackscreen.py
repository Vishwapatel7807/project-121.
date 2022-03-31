from ctypes import resize
from email.mime import image
from tkinter import Frame
import cv2
import numpy as np
import time


print(cv2.__version__)

frame = cv2.VideoWriter_fourcc(*'XVID') 
output_file = cv2.VideoWriter('output.avi', frame, 20.0, (640, 480))

 frame = cv2.resize(frame,(640,480))
 image = cv2.resize(image,(640,480))


# give the camera to warm up
time.sleep(2)
count = 0
background = 0

# Make your path according to your needs
capture_video = cv2.VideoCapture(0)
	

for i in range(60):
	return_val, background = capture_video.read()
	if return_val == False :
		continue

	

background = np.flip(background, axis = 1) # flipping of the frame

# we are reading from video
while (capture_video.isOpened()):
	return_val, img = capture_video.read()
	if not return_val :
		break
	count = count + 1
	img = np.flip(img, axis = 1)

	
	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

	u_black = np.array([104, 153, 70])
    l_black = np.array([30, 30, 0])

	mask = cv2.inRange(frame,l_black,u_black)
	res2 = cv2.bitwise_and(frame, frame, mask = mask)
	

	#-------------------------------------BLOCK----------------------------#
	# ranges should be carefully chosen
	# setting the lower and upper range for mask1
   

	
	
	
	#----------------------------------------------------------------------#

	# the above block of code could be replaced with
	# some other code depending upon the color of your cloth
	

	# Refining the mask corresponding to the detected red color

    #morphologyEx(src, dst, op, kernel) This method accepts the following parameters: ● src − An object representing the source (input) image. ● dst − object representing the destination (output) image
    #● op − An integer representing the type of the Morphological operation. ● kernel − A kernel matrix. morphologyEx() is the method of the class Img Processing which is used to perform operations on a given image
	
	

	# Generating the final output
	f = frame - res
    f = np.where(f == 0,image,f)
