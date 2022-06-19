import cv2
import os




def train():
    video=cv2.VideoCapture(0, cv2.CAP_DSHOW)

    face=cv2.CascadeClassifier('har.xml')


    name=str(input("Enter your name?"))

    path='C:/Users/Pranav/OneDrive/Desktop/Father Day/images/'+name
    os.makedirs(path)
    count=0
    while True:
        ret,frame=video.read()
        faces=face.detectMultiScale(frame,1.3,5)
        for x,y,w,h in faces:
            count=count+1
            name1='./images/'+name+"/"+str(count)+'.jpg'
            print("Creating Image........"+name1)
            cv2.imwrite(name1,frame[y:y+h,x:x+w])
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
        cv2.imshow(name+" Video Capture",frame)
        cv2.waitKey(1)
        if count>499:
            break
    video.release()
    cv2.destroyAllWindows()


















