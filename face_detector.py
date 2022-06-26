import cv2
from random import randrange
# load pre trained data from opencv 
previous_face_data=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# it is for the images 
# img=cv2.imread('virat.jpg')

# for the webcam

webcam=cv2.VideoCapture(0)

while True:
  successful_frame_read,frame=webcam.read()
  black_white_img=cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
  face_coordinates=previous_face_data.detectMultiScale(black_white_img)
  for(x, y, w, h) in face_coordinates:
     cv2.rectangle(frame , (x,y),(x+w,y+h),(randrange(128,256),randrange(128,256),randrange(128,256)),2)
  cv2.imshow('Face Detector App',frame)
  key=cv2.waitKey(1)
  if key==81 or key==113:
    break

webcam.release()

# for the images , use face detection 
"""
#black_white_img=cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
face_coordinates=previous_face_data.detectMultiScale(black_white_img)
print(face_coordinates)
for(x, y, w, h) in face_coordinates:
   cv2.rectangle(img , (x,y),(x+w,y+h),(randrange(128,256),randrange(128,256),randrange(128,256)),2)
#

cv2.imshow('Face Detector App',img)
cv2.waitKey()

print("Hello this is my first app in python")

"""