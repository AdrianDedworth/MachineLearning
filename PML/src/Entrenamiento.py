import cv2
import os
import numpy as np

dataPath = '../static/uploads'
peopleList = os.listdir(dataPath)

#print('Lista de Personas: ', peopleList)

labels = []
facesData = []
label = 1

for nameDir in peopleList:
    usrPath = dataPath + '/' + '1' + '/rostros' #Cambiar el '1' por una variable que contenga el nombre de carpeta
    print("Leyendo imágenes")

    for fileName in os.listdir(usrPath):
        print('Rostros: ', nameDir + '/' + fileName)
        labels.append(label)
        facesData.append(cv2.imread(usrPath + '/' + fileName, 0))
        image = cv2.imread(usrPath + '/' + fileName, 0)

label += 1

faceRecognizer = cv2.face.LBPHFaceRecognizer_create()

print("Entrenando")
faceRecognizer.train(facesData, np.array(labels))

#Almacenar modelo obtenido
os.chdir('../static/modelPeople')
os.mkdir('1') # Cambiar el valor de 1 por una variable de nombre de carpeta
os.chdir('1')
faceRecognizer.write('LBPHFaceMethod.xml')
print("Modelo alamacenado.")