import cv2
from cv2 import resize
from cv2 import scaleAdd 
import numpy as np 

image_path = "image.png"

image = cv2.imread(image_path)

# cv2.imshow('Sample Image ',image)
# directory =r'C:\Users\AbdelrahmanYoussefEl\Documents'

# cv2.waitKey(0)
# cv2.destroyAllWindows()

# filename = 'savedImagestest.png'
# cv2.imwrite(filename , image)
# print("Image was successfully saved ")

# print(image.shape )

# gray = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)
# resize = cv2.resize(image , (200 , 200))

# text = 'Open Cv Tutorial'
# cordinates = (0 ,100)
font = cv2.FONT_HERSHEY_COMPLEX
# fontScale = 0.5 
color = (0,255,0)
thicknes = 2 
# start_point = (0,0)
# end_point = (250 , 200)
# center_point = (100 , 100)
# radius = 80 

center_cord = (50,50)
axis_lenght = (100, 50)

angle = 30 
start_angle = 0 
ending_angle = 360 

image = cv2.ellipse(image , center_cord , axis_lenght , angle , start_angle , ending_angle , color , thicknes)

# top_left = (0 , 0)
# lower_right = (100 , 100)
# image = cv2.rectangle(image , top_left , lower_right , color , thicknes)

# image = cv2.circle(image, center_point , radius , color ,thicknes )

# image = cv2.line(image , start_point , end_point , color , thicknes)
# image = cv2.putText(image , text , cordinates , font , fontScale , color , thicknes)


cv2.imshow('Original Image' , image)
# cv2.imshow('gray Image',gray)
# cv2.imshow(" Resize Image " , resize)
cv2.waitKey(0)
cv2.destroyAllWindows()