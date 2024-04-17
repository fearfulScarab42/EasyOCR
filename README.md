
# EasyOCR


## Librarias


#### Instalar

```
  pip3 install opencv-python easyocr pymupdf pillow flask
```
## Ejecutar el código


```
  python3 EasyOcr.py
```
## API Reference

#### Subir PDF

```http
  POST http://127.0.0.1/uploads
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `file` | `file` | **Requerido**. Archivo de tip PDF |


