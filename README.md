
# EasyOCR

## Autores

- [@fearfulScarab42](https://www.github.com/fearfulScarab42) Diego León Infanzón Meré
- [@AlejandraCebada2](https://www.github.com/AlejandraCebada2) Evelyn Alejandra Cebada Cortés
- [@fedealejandro](https://www.github.com/fedealejandro) Federico Alejandro Vergara Guzmán
- [@TheAdamWaller](https://www.github.com/TheAdamWaller) Pedro Everardo Hernandez Valerio



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

| Parametro | Tipo     | Descripción                |
| :-------- | :------- | :------------------------- |
| `file` | `file` | **Requerido**. Archivo de tip PDF |


