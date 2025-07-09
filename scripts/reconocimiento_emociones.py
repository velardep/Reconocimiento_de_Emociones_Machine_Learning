import cv2        # OpenCV para procesamiento de imágenes y visión por computadora
import os         # Módulo para interactuar con el sistema operativo
import numpy as np

from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

def emotionImage(emotion):
	# Asignar la imagen del emoji correspondiente a la emoción proporcionada
	if emotion == 'Felicidad': image = cv2.imread('Emojis/felicidad.jpeg')
	if emotion == 'Enojo': image = cv2.imread('Emojis/enojo.jpeg')
	if emotion == 'Sorpresa': image = cv2.imread('Emojis/sorpresa.jpeg')
	if emotion == 'Tristeza': image = cv2.imread('Emojis/tristeza.jpeg')
	return image

dataPath = 'C:/Users/Paolo Velarde/Desktop/PROYECTOS/Proyecto_Reconocimiento_Emociones/Data'
imagePaths = os.listdir(dataPath)
print('imagePaths=', imagePaths)


# ----------- Métodos usados para el entrenamiento y lectura del modelo ----------
#method = 'EigenFaces'     # ESTE METODO NO DA TAN BUENOS RESULTADOS AL RECONOCER LOS ROSTROS
#method = 'FisherFaces'    # ESTE MEJORA UN POCO 
method = 'LBPH'            # DE LOS TRES ESTE ES EL MAS OPTIMO

if method == 'EigenFaces':
    emotion_recognizer = cv2.face.EigenFaceRecognizer_create()
elif method == 'FisherFaces':
    emotion_recognizer = cv2.face.FisherFaceRecognizer_create()
elif method == 'LBPH':
    emotion_recognizer = cv2.face.LBPHFaceRecognizer_create()

# Leyendo el modelo
# Cargar el modelo previamente entrenado para el método seleccionado
emotion_recognizer.read(f"modelo{method}.xml")

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# Crear un clasificador en cascada para la detección de rostros
faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Inicializamos las variables
etiquetas_reales = []
etiquetas_predichas = []

# Lista de emociones
emociones = ['Felicidad', 'Enojo', 'Tristeza', 'Sorpresa']

# Inicializar matrices de confusión para cada emoción
matrices_confusion = {emo: np.zeros((len(emociones), len(emociones)), dtype=int) for emo in emociones}


# Bucle principal para el procesamiento de imágenes continuo
while True:
    ret, frame = cap.read()
    if ret == False:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)     # Convertir la imagen a escala de grises para el procesamiento facial
    # Realizar una copia de la imagen en escala de grises para su posterior visualización
    auxFrame = gray.copy()
    
    nFrame = cv2.hconcat([frame, np.zeros((480,300,3),dtype=np.uint8)])
    
    faces = faceClassif.detectMultiScale(gray, 1.3, 5)

    # Comprueba el método utilizado para el reconocimiento de emociones
    for (x, y, w, h) in faces:
        rostro = auxFrame[y:y+h, x:x+w]
        rostro = cv2.resize(rostro, (150, 150), interpolation=cv2.INTER_CUBIC)
        result = emotion_recognizer.predict(rostro)
        
        # Inicializamos la variable
        label = 0
        
        # Asumiendo que 'label' es la emoción real
        etiquetas_reales.append(label)
        etiquetas_predichas.append(result[0])

        # Actualizar matriz de confusión correspondiente a la emoción
        matrices_confusion[emociones[label]][result[0]] += 1
        
        
        cv2.putText(frame, '{}'.format(result), (x, y-5), 1, 1.3, (255, 255, 0), 1, cv2.LINE_AA)


        if method == 'EigenFaces':
            # Verifica si la similitud entre el rostro reconocido y el rostro de entrenamiento es menor que un umbral (5700)
            # El umbral actúa como un criterio de aceptación para el rostro reconocido, en este caso con EigenFaces trabaja con umbrales arriba de 1000
            if result[1] < 5700:     
                # Muestra el nombre de la emoción sobre el fotograma
                cv2.putText(frame, '{}'.format(imagePaths[result[0]]), (x, y-25), 2, 1.1, (0, 255, 0), 1, cv2.LINE_AA)
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                image = emotionImage(imagePaths[result[0]])
                nFrame = cv2.hconcat([frame, image])
            else:
                cv2.putText(frame, 'Neutral o Compuesto', (x, y-20), 2, 0.8, (0, 0, 255), 1, cv2.LINE_AA)
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
                nFrame = cv2.hconcat([frame, np.zeros((480,300,3),dtype=np.uint8)])



        elif method == 'FisherFaces':
            # Verifica si la similitud entre el rostro reconocido y el rostro de entrenamiento es menor que un umbral (500)
            # El umbral actúa como un criterio de aceptación para el rostro reconocido, en este caso con FisherFaces trabaja con umbrales arriba de 100
            if result[1] < 500:       
                # Muestra el nombre de la emoción sobre el fotograma
                cv2.putText(frame, '{}'.format(imagePaths[result[0]]), (x, y-25), 2, 1.1, (0, 255, 0), 1, cv2.LINE_AA)
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                image = emotionImage(imagePaths[result[0]])
                nFrame = cv2.hconcat([frame, image])
            else:
                cv2.putText(frame, 'Neutral o Compuesto', (x, y-20), 2, 0.8, (0, 0, 255), 1, cv2.LINE_AA)
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
                nFrame = cv2.hconcat([frame, np.zeros((480,300,3),dtype=np.uint8)])



        elif method == 'LBPH':
            # Verifica si la similitud entre el rostro reconocido y el rostro de entrenamiento es menor que un umbral (70)
            # El umbral actúa como un criterio de aceptación para el rostro reconocido, en este caso con LBPH trabaja con umbrales arriba de 10
            if result[1] < 70:          
                # Muestra el nombre de la emoción sobre el fotograma
                cv2.putText(frame, '{}'.format(imagePaths[result[0]]), (x, y-25), 2, 1.1, (0, 255, 0), 1, cv2.LINE_AA)
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                image = emotionImage(imagePaths[result[0]])
                nFrame = cv2.hconcat([frame, image])
            else:
                cv2.putText(frame, 'Neutral o Compuesto', (x, y-20), 2, 0.8, (0, 0, 255), 1, cv2.LINE_AA)
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
                nFrame = cv2.hconcat([frame, np.zeros((480,300,3),dtype=np.uint8)])

    # Espera la pulsación de la tecla ESC (27) o hasta que se capturen 200 rostros
    cv2.imshow('nFrame', nFrame)
    k = cv2.waitKey(1)
    if k == 27:
        break

# Cierra la ventana de la camara 
cap.release()
cv2.destroyAllWindows()


# Calcular métricas para cada emocion

# Calcula una matriz de confucion para tener una aproximacion de que emocion se registra mas 
# Ejemplo
    #   [[139 139 139 139]   [[enojo     139      139        139]   
    #   [ 61  61  61  61]    [ 61     felicidad   61          61]
    #   [ 45  45  45  45]    [ 45         45   sorpresa       45]
    #   [  4   4   4   4]]   [  4         4        4    tristeza]]

for emociones, matriz_confusion in matrices_confusion.items():
    print(f'Matriz de Confusión:\n{matriz_confusion}')
    break


# Calcular Sensibilidad y el Soporte
for emocion, matriz_confusion in matrices_confusion.items():
    # Sensibilidad, indica la proporción de casos de cada emoción que el modelo ha identificado correctamente
    sensibilidad = matriz_confusion[0, 0] / np.sum(matriz_confusion[0, :])
    # Precisión, indica la proporción de casos identificados como Enojo que son realmente Enojo
    precision = matriz_confusion[0, 0] / np.sum(matriz_confusion[:, 0])
    # F1-score, combina la precisión y la sensibilidad en una sola métrica
    f1_score = 2 * (precision * sensibilidad) / (precision + sensibilidad)
    print('-------------------ENOJO-----------------------')
    print(f'Sensibilidad: {sensibilidad}')
    print(f'Precisión: {precision}')
    print(f'F1-score: {f1_score}')
    break
    
for emocion, matriz_confusion in matrices_confusion.items():
    # Sensibilidad, indica la proporción de casos de cada emoción que el modelo ha identificado correctamente
    sensibilidad = matriz_confusion[1, 1] / np.sum(matriz_confusion[0, :])
    # Precisión, indica la proporción de casos identificados como Felicidad que son realmente Felicidad
    precision = matriz_confusion[1, 1] / np.sum(matriz_confusion[:, 0])
    # F1-score, combina la precisión y la sensibilidad en una sola métrica
    f1_score = 2 * (precision * sensibilidad) / (precision + sensibilidad)
    print('-------------------FELICIDAD-----------------------')
    print(f'Sensibilidad: {sensibilidad}')
    print(f'Precisión: {precision}')
    print(f'F1-score: {f1_score}')
    break

for emocion, matriz_confusion in matrices_confusion.items():
    # Sensibilidad, indica la proporción de casos de cada emoción que el modelo ha identificado correctamente
    sensibilidad = matriz_confusion[2, 2] / np.sum(matriz_confusion[0, :])
    # Precisión, indica la proporción de casos identificados como Sorpresa que son realmente Sorpresa
    precision = matriz_confusion[2, 2] / np.sum(matriz_confusion[:, 0])
    # F1-score, combina la precisión y la sensibilidad en una sola métrica
    f1_score = 2 * (precision * sensibilidad) / (precision + sensibilidad)
    print('-------------------SORPRESA-----------------------')
    print(f'Sensibilidad: {sensibilidad}')
    print(f'Precisión: {precision}')
    print(f'F1-score: {f1_score}')
    break

for emocion, matriz_confusion in matrices_confusion.items():
    # Sensibilidad, indica la proporción de casos de cada emoción que el modelo ha identificado correctamente
    sensibilidad = matriz_confusion[3, 3] / np.sum(matriz_confusion[0, :])
    # Precisión, indica la proporción de casos identificados como Tristeza que son realmente Tristeza
    precision = matriz_confusion[3, 3] / np.sum(matriz_confusion[:, 0])
    # F1-score, combina la precisión y la sensibilidad en una sola métrica donde si se acerca a 1 es optimo y si esta cerca de 0 no lo es
    f1_score = 2 * (precision * sensibilidad) / (precision + sensibilidad)
    print('-------------------TRISTEZA-----------------------')
    print(f'Sensibilidad: {sensibilidad}')
    print(f'Precisión: {precision}')
    print(f'F1-score: {f1_score}')
    break


# Calcula el promedio de los scores F1
promedio_f1 = np.mean(f1_score)
print('------------------------------------------')
# Para tener una idea de que tan optimo es el modelo, podemos tomar el promedio de los f1_score donde si esta cerca de 0 es poco optimo y si esta 
# cerca a 1 si lo es
# aunque dependera mucho del tiempo que se ejecute el modelo
print(f'Promedio total de F1-score: {promedio_f1}')  

 # TODAS LAS METRICAS CALCULADAS DEPENDERAN MUCHO DEL TIEMPO QUE SE REGISTRE CADA EMOCION 


#---------------AQUI SE SUBEN NUEVOS ROSTROS PARA VER SI EXISTE SIMILITUD CON LOS QUE ENTRENAMOS