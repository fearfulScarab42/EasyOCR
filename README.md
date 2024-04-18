
# EasyOCR

Es una biblioteca de Python que proporciona una solución fácil de usar para realizar reconocimiento óptico de caracteres (OCR). Con EasyOCR, puedes extraer texto de imágenes de manera rápida y precisa, lo que lo convierte en una herramienta poderosa para una variedad de aplicaciones, como procesamiento de documentos, automatización de tareas y análisis de imágenes.

EasyOCR utiliza técnicas de procesamiento de imágenes y aprendizaje automático para reconocer texto en imágenes. Aquí hay un resumen de cómo funciona:

- **Preprocesamiento de imágenes**: Antes de realizar el reconocimiento óptico de caracteres, la imagen de entrada puede pasar por varios pasos de preprocesamiento, como ajuste de contraste, eliminación de ruido y mejora de la calidad de la imagen. Esto ayuda a mejorar la precisión del reconocimiento.

- **Detección de texto**: EasyOCR utiliza algoritmos de detección de texto para identificar las regiones de la imagen que contienen texto. Esto puede implicar la segmentación de la imagen en regiones candidatas que podrían contener texto, utilizando técnicas como detección de contornos o algoritmos de detección de objetos.

- **Reconocimiento de caracteres**: Una vez que se detectan las regiones de texto, EasyOCR utiliza modelos de aprendizaje automático entrenados para reconocer los caracteres en esas regiones. Estos modelos están entrenados en grandes conjuntos de datos que contienen imágenes de texto junto con las etiquetas de los caracteres correspondientes.

- **Postprocesamiento**: Después de reconocer los caracteres, es posible que se realicen pasos adicionales de postprocesamiento para mejorar la precisión o el formato del texto reconocido. Esto puede incluir la corrección de errores, la eliminación de caracteres no deseados o la reconstrucción de palabras mal segmentadas.

## Autores

- [@fearfulScarab42](https://www.github.com/fearfulScarab42) Diego León Infanzón Meré
- [@AlejandraCebada2](https://www.github.com/AlejandraCebada2) Evelyn Alejandra Cebada Cortés
- [@fedealejandro](https://www.github.com/fedealejandro) Federico Alejandro Vergara Guzmán
- [@TheAdamWaller](https://www.github.com/TheAdamWaller) Pedro Everardo Hernandez Valerio


## Versiones

### Versión de python utilizada

- Python >= 3.10.*

#### Versión de Librarias

- Flask==3.0.0
- opencv-contrib-python==4.8.1.78
- opencv-python==4.8.1.78
- opencv-python-headless==4.9.0.80
- easyocr==1.7.1
- PyMuPDF==1.24.1
- PyMuPDFb==1.24.1
- Pillow==10.0.1
- Werkzeug==3.0.0


#### Instalar
```
  git clone https://github.com/fearfulScarab42/EasyOCR.git
```

```
  cd EasyOCR
```

```
  pip3 install opencv-python easyocr pymupdf pillow flask Werkzeug
```
## Ejecutar el código


```
  python3 EasyOcr.py
```
## API referencia

#### Subir PDF

```http
  POST http://127.0.0.1:5000/uploads
```

| Parametro | Tipo     | Descripción                |
| :-------- | :------- | :------------------------- |
| `file` | `file` | **Requerido**. Archivo de tipo PDF |

#### Ejemplo de petición en Postman


![Logo](https://raw.githubusercontent.com/fearfulScarab42/EasyOCR/main/Postman.png)

#### Ejemplo de response exitoso


![Logo](https://raw.githubusercontent.com/fearfulScarab42/EasyOCR/main/response.png)
