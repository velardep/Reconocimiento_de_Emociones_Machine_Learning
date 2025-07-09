# Reconocimiento de Emociones con Machine Learning

Sistema integrado para la captura, entrenamiento y reconocimiento de emociones faciales en tiempo real mediante visión artificial y aprendizaje automático. Este proyecto utiliza Python con OpenCV y modelos clásicos de reconocimiento facial para detectar y clasificar emociones a partir de imágenes capturadas por cámara.

---

## Descripción

Este sistema consta de tres módulos principales que trabajan de forma integrada para ofrecer un flujo completo de reconocimiento emocional:

1. **Captura de Emociones:** Captura imágenes faciales desde la cámara, clasificadas por emoción (Felicidad, Enojo, Tristeza, Sorpresa). Las imágenes se guardan en carpetas específicas para cada emoción.

2. **Entrenamiento de Modelos:** Lee las imágenes capturadas y entrena tres modelos clásicos de reconocimiento facial basados en aprendizaje automático: EigenFaces, FisherFaces y LBPH. Muestra en consola (y en la interfaz) el tiempo de entrenamiento y detalles.

3. **Reconocimiento en Tiempo Real:** Usa los modelos entrenados para reconocer emociones faciales en imágenes de video capturadas en vivo por la cámara.

---

## Características principales

- Captura y almacenamiento organizado de imágenes faciales por emoción.
- Entrenamiento con tres modelos clásicos y probados en visión computacional: EigenFaces, FisherFaces y LBPH.
- Reconocimiento en vivo con actualización constante.
- Interfaz gráfica con Tkinter que permite controlar todo el flujo: captura, entrenamiento y reconocimiento.
- Visualización de resultados e información en consola e interfaz.
- Cierre seguro de procesos y manejo de subprocesos para tareas en background.

---

## Tecnologías usadas

- **Python 3.13** para todo el desarrollo.
- **OpenCV (contrib)** para visión artificial y reconocimiento facial.
- **imutils** para procesamiento de imágenes.
- **Tkinter** para la interfaz gráfica.
- Modelos clásicos de reconocimiento facial basados en aprendizaje automático (no deep learning).
- Subprocesos para ejecución paralela y manejo de tareas sin bloquear la interfaz.

---

## Instalación y ejecución

### Requisitos previos

- Sistema operativo: Windows (probado en Windows 10 y 11).
- Python 3.13 instalado y agregado al PATH.
- Cámara web conectada y funcional.

### Pasos para configurar el entorno

1. **Instalar Python 3.13**

   Descarga e instala desde [https://www.python.org/downloads/](https://www.python.org/downloads/).  
   Asegúrate de marcar "Add Python to PATH" durante la instalación.

2. **Instalar las librerías necesarias**

   Abre una terminal y ejecuta:

   ```bash
   pip install opencv-contrib-python imutils
