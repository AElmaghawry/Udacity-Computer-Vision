import cv2
from numpy import disp, size 

img = cv2.imread("image.png")
img_green = img[:,:,0]
cv2.imshow("output",img_green) 
disp(size(img))
cv2.waitKey(0)