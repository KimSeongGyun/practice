import cv2
import numpy as np

def checkcolor(hsvimage):
	lower_orange = np.array([0,50,100])
	upper_orange = np.array([10,255,255])
	maskorange = cv2.inRange(hsvimage, lower_orange, upper_orange)

	return maskorange

if __name__=='__main__':
	original_image = cv2.imread('rubber4.jpg')
	resize = cv2.resize(original_image, None, fx = 0.2, fy = 0.2 )
	hsv_image = cv2.cvtColor(resize, cv2.COLOR_BGR2HSV)
	output = checkcolor(hsv_image)
	cv2.imshow('resized', resize)
	cv2.imshow('output', output)
	cv2.waitKey(0)
