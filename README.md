
# EasyOCR

Es una biblioteca de Python que proporciona una solución fácil de usar para realizar reconocimiento óptico de caracteres (OCR). Con EasyOCR, puedes extraer texto de imágenes de manera rápida y precisa, lo que lo convierte en una herramienta poderosa para una variedad de aplicaciones, como procesamiento de documentos, automatización de tareas y análisis de imágenes.

## Autores

- [@fearfulScarab42](https://www.github.com/fearfulScarab42) Diego León Infanzón Meré
- [@AlejandraCebada2](https://www.github.com/AlejandraCebada2) Evelyn Alejandra Cebada Cortés
- [@fedealejandro](https://www.github.com/fedealejandro) Federico Alejandro Vergara Guzmán
- [@TheAdamWaller](https://www.github.com/TheAdamWaller) Pedro Everardo Hernandez Valerio


## Librarias

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


