import cv2
import os
import numpy as np
import time

# Función para obtener y almacenar el modelo de reconocimiento facial según el método especificado.
def obtenerModelo(method,facesData,labels):
	if method == 'EigenFaces': emotion_recognizer = cv2.face.EigenFaceRecognizer_create()
	if method == 'FisherFaces': emotion_recognizer = cv2.face.FisherFaceRecognizer_create()
	if method == 'LBPH': emotion_recognizer = cv2.face.LBPHFaceRecognizer_create()

	# Entrenando el reconocedor de rostros
	print("Entrenando ( "+method+" )...")
	inicio = time.time()
	emotion_recognizer.train(facesData, np.array(labels))
	tiempoEntrenamiento = time.time()-inicio
	print("Tiempo de entrenamiento ( "+method+" ): ", tiempoEntrenamiento)

	# Almacenando el modelo obtenido
	emotion_recognizer.write("modelo"+method+".xml")

dataPath = dataPath = 'C:/Users/Paolo Velarde/Desktop/PROYECTOS/Proyecto_Reconocimiento_Emociones/Data' # Ruta donde esta almacenado Data
emotionList = os.listdir(dataPath)
print('Lista de personas: ', emotionList)

# Lista de emociones (nombres de carpetas)
labels = []     # Lista para almacenar las etiquetas asociadas a cada rostro
facesData = []     # Lista para almacenar las imágenes de rostros
label = 0

# Iterar sobre las carpetas de emociones
for nameDir in emotionList:
	emotionPath = dataPath + '/' + nameDir
	print('Leyendo las imágenes')

    # Iterar sobre las imágenes de rostros en la carpeta de la emoción actual
	for fileName in os.listdir(emotionPath):
		labels.append(label)
		facesData.append(cv2.imread(emotionPath+'/'+fileName,0))
		image = cv2.imread(emotionPath+'/'+fileName,0)
		
	label = label + 1

# Obtener y almacenar el modelo para cada método de reconocimiento facial
obtenerModelo('EigenFaces',facesData,labels)
obtenerModelo('FisherFaces',facesData,labels)
obtenerModelo('LBPH',facesData,labels)

#------AQUI UNA VEZ GUARDADOS LOS ROSTROS, SE EJECUTA ESTO PARA QUE EL MODELO DE ENTRENE