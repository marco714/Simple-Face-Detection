import cv2
from random import randrange
# Load some pre-trained data on face frontals from opencv(haar cascade algorithm)
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#Choose an image to detect face in
#img = cv2.imread('Pictures1/allFace.jpg')
webcam = cv2.VideoCapture(0)
#key = cv2.waitKey(1)

#Iterate forever over frames
while True:

    successful_frame_read, frame = webcam.read()

    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (randrange(256), randrange(256), randrange(256)), 5)
        print(face_coordinates)
    
    cv2.imshow('Marco Detector', frame)
    key = cv2.waitKey(1)

    if key == 81 or key == 113:
        break

#Release the video capture
webcam.release()

"""
#Draw Rectangles around the faces

for (x, y, w, h) in face_coordinates:  
    #It is face_coordinates zero because it a list inside a one list 
    #(x, y, w, h) = face_coordinates[0]
    cv2.rectangle(img, (x, y), (x + w, y + h), (randrange(256), randrange(256), randrange(256)), 5) 

 

#print(face_coordinates)
# Display The images     
cv2.imshow('Clever Programmer Face Detector', img) 
cv2.waitKey()
 
"""
print("Code Completed") 

