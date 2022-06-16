import cv2
import os

def videoStreaming():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    faceDetector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    datapath = 'C:/Users/max12/GIT_PULLS/MachineLearning/PML/static/modelPeople'
    usrids = os.listdir(datapath) # se obtiene una lista de los id's de usuarios [1,2,3...]

    faceRecognizer = cv2.face.LBPHFaceRecognizer_create()

    #Lectura de archivos de entranamiento
    for usrid in usrids:
        modelPath = datapath + '/' + usrid
        faceRecognizer.read(modelPath)

    while True:
        ret, frame = cap.read()
        if ret:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            auxFrame = gray.copy()
            faces = faceDetector.detectMultiScale(gray, 1.3, 5)
            for(x,y,w,h) in faces:
                rostro = auxFrame[y:y+h,x:x+w]
                rostro = cv2.resize(rostro,(150,150), interpolation=cv2.INTER_CUBIC)
                result = faceRecognizer.predict(rostro)

                cv2.putText(frame, '{}'.format(result), (x,y-5), 1, 1.3, (255,255,0), 1, cv2.LINE_AA)

                #Reconocimiento Facial
                if result[1] < 90:
                    cv2.putText(frame, 'Permitido', (x,y-25), 2, 1.5, (0,255,0), 1, cv2.LINE_AA) #quitar imagePaths ('{}'.format(imagePaths[result[0]]))
                    cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
                else:
                    cv2.putText(frame, 'Desconocido', (x,y-20), 2, 1.5, (0,0,255), 1, cv2.LINE_AA)
                    cv2.rectangle(frame, (x,y), (x+w,y+h), (0,0,255), 2)
                    #Notificar sobre intrusos
            (flag, encodedImage) = cv2.imencode(".jpg", frame)
            if not flag:
                continue
            yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(encodedImage) + b'\r\n')