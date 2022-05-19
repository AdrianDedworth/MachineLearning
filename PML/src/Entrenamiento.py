import cv2
import os
import numpy as np

dataPath = 'static/uploads'
peopleList = os.listdir(dataPath)

#print('Lista de Personas: ', peopleList)

labels = []
facesData = []
label = 1

for nameDir in peopleList:
    usrPath = dataPath + '/' + nameDir
    print("Leyendo imágenes")