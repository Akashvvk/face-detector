import cv2
trained_face_data=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

webcam=cv2.VideoCapture(0)
while True:
    successfulframe,frame =webcam.read()
    greyscaled_img=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face_coordinates=trained_face_data.detectMultiScale(greyscaled_img)
    for (x,y,w,h) in face_coordinates:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
    cv2.imshow("clevervvk face detector",frame)
    key=cv2.waitKey(1)
    if key==81 or key==113:
        break
webcam.release()
print("code complete")