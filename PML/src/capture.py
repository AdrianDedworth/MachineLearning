import cv2
import imutils
from src.GetID import GetID

def CaptureFace():
    usrID = GetID()
    videoPath = 'C:/Users/max12/GIT_PULLS/MachineLearning/PML/static/uploads/'

    pathToSavePhotos = videoPath + str(usrID) + '/rostros'

    videoPath = videoPath + str(usrID)

    cap = cv2.VideoCapture(videoPath + '/' + str(usrID) + '.mp4')

    faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
    count = 0

    while True:
        ret, frame = cap.read()
        if ret == False: break
        frame = imutils.resize(frame, width=640)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        auxframe = frame.copy()

        faces = faceClassif.detectMultiScale(gray, 1.3, 5)

        for(x,y,w,h) in faces:
            cv2.rectangle(frame, (x,y), (x+w, +h), (0,255,0), 2)
            rostro = auxframe[y:y+h,x:x+w]
            rostro = cv2.resize(rostro, (150,150),interpolation=cv2.INTER_CUBIC)
            cv2.imwrite(pathToSavePhotos + '/rostro_{}.jpg'.format(count), rostro)
            count += 1
        cv2.imshow('frame', frame)

        k = cv2.waitKey(1)
        if k == 27 or count >= 300:
            break
    cap.release()
    cv2.destroyAllWindows()