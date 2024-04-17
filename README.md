
# EasyOCR

## Autores

- [@fearfulScarab42](https://www.github.com/fearfulScarab42)
- [@AlejandraCebada2](https://www.github.com/AlejandraCebada2)
- [@fedealejandro](https://www.github.com/fedealejandro)
- [@TheAdamWaller](https://www.github.com/TheAdamWaller)



## Librarias


#### Instalar

```
  pip3 install opencv-python easyocr pymupdf pillow flask
```
## Ejecutar el código


```
  python3 EasyOcr.py
```
## API referencia

#### Subir PDF

```http
  POST http://127.0.0.1/uploads
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `file` | `file` | **Requerido**. Archivo de tip PDF |


