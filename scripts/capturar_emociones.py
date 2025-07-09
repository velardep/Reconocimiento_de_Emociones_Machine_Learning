import cv2        # OpenCV para procesamiento de imágenes y visión por computadora
import os         # Módulo para interactuar con el sistema operativo
import imutils    # Funciones auxiliares para manipular imágenes de manera sencilla

# Define la emoción que se está reconociendo y se almacena en una carpeta con el mismo nombre (comentar o descomentar según la emoción deseada)
#emotionName = 'Enojo'
#emotionName = 'Felicidad'
#emotionName = 'Sorpresa'
#emotionName = 'Tristeza'
import sys
emotionName = sys.argv[1] if len(sys.argv) > 1 else 'Felicidad'  # Valor por defecto


# Ruta donde se almacenan los datos (imágenes) para el reconocimiento de emociones
dataPath = 'C:/Users/Paolo Velarde/Desktop/PROYECTOS/Proyecto_Reconocimiento_Emociones/Data' # Ruta donde esta almacenado Data
emotionsPath = dataPath + '/' + emotionName

# Verifica si la carpeta para la emoción específica ya existe, y si no, la crea
if not os.path.exists(emotionsPath):
	print('Carpeta creada: ',emotionsPath)
	os.makedirs(emotionsPath)

# Inicia la captura de video desde la cámara (0 indica la cámara predeterminada)
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

# Carga el clasificador HaarCascade para la detección de rostros
faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
# Inicializa el contador de rostros capturados
count = 0

# Bucle principal para capturar y procesar imágenes desde la cámara
while True:

	ret, frame = cap.read()      # Captura un fotograma de la cámara
	if ret == False: break       # Verifica si la captura fue exitosa
	frame =  imutils.resize(frame, width=640)        # Redimensiona el fotograma para tener un ancho de 640 píxeles
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)       # Convierte el fotograma a escala de grises para facilitar el procesamiento
	auxFrame = frame.copy()       # Crea una copia auxiliar del fotograma en color para visualización

	faces = faceClassif.detectMultiScale(gray,1.3,5)        # Detecta rostros en la imagen en escala de grises

    # Itera sobre los rostros detectados
	for (x,y,w,h) in faces:
        # Dibuja un rectángulo alrededor de cada rostro detectado
		cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
        # Recorta y redimensiona el área del rostro para ser almacenada como imagen
		rostro = auxFrame[y:y+h,x:x+w]
		rostro = cv2.resize(rostro,(150,150),interpolation=cv2.INTER_CUBIC)
        # Guarda la imagen del rostro en la carpeta correspondiente a la emoción
		cv2.imwrite(emotionsPath + '/rotro_{}.jpg'.format(count),rostro)
        # Incrementa el contador de rostros capturados
		count = count + 1  
    # Muestra el fotograma con los rectángulos dibujados alrededor de los rostros
	cv2.imshow('frame',frame)  

    # Espera la pulsación de la tecla ESC (27) o hasta que se capturen 200 rostros
	k =  cv2.waitKey(1)
	if k == 27 or count >= 200:
		break

# Libera los recursos de la cámara y cierra todas las ventanas
cap.release()
cv2.destroyAllWindows()

#------------AQUI SE SUBEN LOS ROSTROS Y SE GUARDAN EN DATA

