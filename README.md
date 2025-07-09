<p align="center">
  <a href="https://www.python.org" target="_blank">
    <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" width="160" alt="Python Logo">
  </a>
</p>

# Reconocimiento de Emociones con Machine Learning

Sistema integrado para la captura, entrenamiento y reconocimiento en tiempo real de emociones faciales mediante visión artificial y aprendizaje automático. Este proyecto utiliza Python con OpenCV y modelos clásicos de reconocimiento facial para detectar y clasificar emociones a partir de imágenes capturadas por cámara.

---

## Descripción

Este sistema consta de tres módulos principales que trabajan integrados para ofrecer un flujo completo y dinámico de reconocimiento emocional:

1. **Captura de Emociones:**  
   Captura imágenes faciales desde la cámara, clasificadas por emoción (Felicidad, Enojo, Tristeza, Sorpresa). Las imágenes se guardan organizadamente en carpetas específicas para cada emoción.  
   El usuario puede seleccionar la emoción que desea capturar mediante una interfaz gráfica sencilla.

2. **Entrenamiento de Modelos:**  
   Lee las imágenes capturadas y entrena tres modelos clásicos y probados de reconocimiento facial basados en aprendizaje automático:  
   - EigenFaces  
   - FisherFaces  
   - LBPH (Local Binary Patterns Histograms)  
   Muestra en consola y en la interfaz el progreso y tiempo de entrenamiento de cada modelo.

3. **Reconocimiento en Tiempo Real:**  
   Utiliza los modelos entrenados para reconocer emociones faciales en imágenes de video capturadas en vivo por la cámara. La interfaz gráfica permite iniciar y cerrar el reconocimiento dinámicamente.

---

## Características principales

- Captura y almacenamiento organizado de imágenes faciales por emoción.
- Entrenamiento simultáneo con tres modelos clásicos de reconocimiento facial.
- Reconocimiento en vivo con actualizaciones constantes y resultados visibles.
- Interfaz gráfica en Tkinter para controlar captura, entrenamiento y reconocimiento desde un solo lugar.
- Visualización en tiempo real del progreso del entrenamiento y notificaciones de estado.
- Manejo seguro de procesos en background para no bloquear la interfaz.
- Opciones para cerrar procesos y salir de forma segura.

---

## Tecnologías usadas

- **Python 3.13** como lenguaje principal.
- **OpenCV (opencv-contrib-python)** para visión computacional y detección facial.
- **imutils** para funciones auxiliares de procesamiento de imágenes.
- **Tkinter** para interfaz gráfica de usuario.
- **Modelos clásicos de reconocimiento facial:** EigenFaces, FisherFaces, LBPH.  
  Estos modelos son métodos tradicionales de machine learning, no deep learning.
- Uso de subprocesos (`subprocess`, `threading`) para ejecución paralela y evitar bloqueo.

---

## Instalación y ejecución

### Requisitos previos

- Windows 10 o 11 (probado).
- Python 3.13 instalado y agregado al PATH.
- Cámara web conectada y funcionando.

### Pasos para configurar el entorno

1. **Instalar Python 3.13**  
   Descargar desde [https://www.python.org/downloads/](https://www.python.org/downloads/) y marcar "Add Python to PATH".

2. **Instalar las librerías necesarias**  
   Ejecutar en terminal:

   ```bash
   pip install opencv-contrib-python imutils

## Uso

1. Clona este repositorio o descarga el código.

2. Asegúrate de que los scripts estén en la carpeta `scripts` (o actualiza las rutas según tu estructura).

3. Ejecuta la interfaz principal:

   ```bash
   python interfaz.py

## Notas importantes

- Los modelos entrenados se guardan en archivos `.xml` generados automáticamente durante el entrenamiento.
- Estos archivos `.xml` se **sobrescriben** al volver a entrenar los modelos.
- Debido a su tamaño, los archivos `.xml` de los modelos **no se suben a GitHub**. Debes generarlos localmente tras entrenar.
- El sistema utiliza modelos **clásicos de Machine Learning** para reconocimiento facial: `EigenFaces`, `FisherFaces` y `LBPH`.
- No utiliza redes neuronales profundas (**Deep Learning**).
- Para obtener mejores resultados, se recomienda capturar y entrenar con **suficientes imágenes por emoción** (mínimo 200 por categoría).
