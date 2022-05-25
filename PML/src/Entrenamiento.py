import cv2
import os
import numpy as np
from src.GetID import GetID

def TrainingSystem():
    usrID = GetID()
    dataPath = 'C:/Users/max12/GIT_PULLS/MachineLearning/PML/static/uploads/'
    peopleList = os.listdir(dataPath)

    #print('Lista de Personas: ', peopleList)

    labels = []
    facesData = []
    label = usrID

    for nameDir in peopleList:
        usrPath = dataPath + '/' + str(usrID) + '/rostros'
        print("Leyendo imágenes")

        for fileName in os.listdir(usrPath):
            print('Rostros: ', nameDir + '/' + fileName)
            labels.append(label)
            facesData.append(cv2.imread(usrPath + '/' + fileName, 0))
            #image = cv2.imread(usrPath + '/' + fileName, 0)

    faceRecognizer = cv2.face.LBPHFaceRecognizer_create()

    print("Entrenando")
    faceRecognizer.train(facesData, np.array(labels))

    #Almacenar modelo obtenido
    os.chdir('C:/Users/max12/GIT_PULLS/MachineLearning/PML/static/modelPeople')
    os.mkdir(str(usrID))
    os.chdir(str(usrID))
    trainingFile = str(usrID) + '.xml'
    faceRecognizer.write(trainingFile)
    print("Modelo alamacenado.")
    statusMessage = "Entrenamiento Terminado Exitosamente"
    return statusMessage