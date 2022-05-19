import cv2
import imutils

def CaptureFace():
    dataPath = 'static/uploads/'

    #path = path.split('/')
    #vid_name = path[1]

    dataPath = dataPath + '1/' #path[0]
    #print(vid_name)

    cap = cv2.VideoCapture(dataPath + 'test_video.mp4')

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
            cv2.imwrite(dataPath + '/rostro_{}.jpg'.format(count), rostro)
            count += 1
        cv2.imshow('frame', frame)

        k = cv2.waitKey(1)
        if k == 27 or count >= 60:
            break
    cap.release()
    cv2.destroyAllWindows()

CaptureFace()