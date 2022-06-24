from tokenize import PlainToken
import numpy as np
import cv2
from cv2 import aruco
import matplotlib.pyplot as plt

arucoDic = aruco.getPredefinedDictionary(dict = aruco.DICT_6X6_250)
image = aruco.drawMarker(arucoDic, 0, 600, 1)
# drawMarker(Dictionary, id = 0, total_Pixel_size = 600, border = 1)

print(image.shape)
print("ArUco Marker is created!")

cv2.imshow("AruCo Marker", image) # Show image file
cv2.imwrite("AruCo Marker.png", image) # Save image file
cv2.waitKey() # Maintain until keyboard input