import cv2 

# img = cv2.imread('image.png',-1)
# cv2.imshow('Original Image', img)

# cv2.waitKey(0)
# cv2.destroyAllWindows()
# this method is also used to capture a video form a file
cam = cv2.VideoCapture('Captured_video.mp4')
# cam = cv2.VideoCapture(1)
# # to check weather camera is connected or not 
# if (cam.isOpened () == False):
#     # print the camera is not connected 
#     print("Camera could't open")

# # to get the width and hight form the camera feed 
# frame_width = int(cam.get(3))
# frame_hight = int(cam.get(4))

# # video codded >>>>> encoders , and decoders 

# # saving the video with the concded variables 
# video_code = cv2.VideoWriter_fourcc(*'XVID')
# video_output = cv2.VideoWriter('Captured_video.mp4', video_code , 30 , (frame_width , frame_hight))


# # make a loop to get all the frames that is being stramed from the camera 

while (True):
#     # ret value to check if the camera gives a feed or not 
#     # frame is the frame that is recorded 
    ret , frame = cam.read()
    cv2.imshow('Camera feed', frame)
#     # to check if there is a stream from the camera or not 
#     if ret == True:
#         #  video write the streamed feed 
#         video_output.write(frame)
#         # show the stream from the camera 
        # cv2.imshow('Camera feed', frame) 
# # # This method to close the stream of the webcam 0XFF is asci code command for the quite 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#     else:
#         break
cam.release()
cv2.destroyAllWindows()
# # to print in terminal what is happend 
# print(" The video was saved sucessfully")