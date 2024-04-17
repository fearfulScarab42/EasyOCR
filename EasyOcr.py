#Evelyn Alejandra Cebada Cortes
#Actividad/Tarea de clase.

from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os
import cv2
import easyocr
import fitz
from PIL import Image

app = Flask(__name__)

UPLOAD_FOLDER = '.'  # Directorio de carga de archivos
ALLOWED_EXTENSIONS = {'pdf'}  # Extensiones de archivo permitidas
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER  # Configurar el directorio de carga de archivos en la aplicación Flask

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def pdf2png(file_name):
    directory_path = "./Output_files/"
    base_name = os.path.splitext(os.path.basename(file_name))[0]
    generated_files = []

    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        print(f"Directory '{directory_path}' created successfully.")

    existing_files = [f for f in os.listdir(directory_path) if f.startswith(base_name) and f.endswith('.png')]
    if existing_files:
        generated_files = [os.path.join(directory_path, f) for f in existing_files]

    pdf_document = fitz.open(file_name)
    for page_number in range(pdf_document.page_count):
        page = pdf_document.load_page(page_number)
        img = page.get_pixmap(matrix=fitz.Matrix(600/300, 600/300))
        img_pillow = Image.frombytes("RGB", [img.width, img.height], img.samples)
        new_file_name = f"{directory_path}{base_name}_{page_number + 1}.png"
        if os.path.exists(new_file_name):
            print(f"File '{new_file_name}' already exists. Skipping...")
        else:
            img_pillow.save(new_file_name, "PNG")
            generated_files.append(new_file_name)
            print(f"File '{new_file_name}' save successfully.")
    
    pdf_document.close()
    return generated_files

class Reader():
    @staticmethod
    def read_img(img_path):
        img = cv2.imread(img_path)
        return img
    
    def __init__(self):
        languages = ['en','es','fr','de','it','pt']
        self.reader = easyocr.Reader(languages, model_storage_directory=os.path.join('models'), download_enabled=True)
    
    def __call__(self, img):
        return self.extract_text(img)
    
    def extract_text(self, img):
        result = self.reader.readtext(img)
        extracted_text = []
        for text in filter(lambda x: x[-1] > .45, result):
            box, acc_text, confidence = text
            img = cv2.rectangle(img, [int(i) for i in box[0]], [int(i) for i in box[2]], (0, 255, 0), 2)
            extracted_text.append(acc_text)
        return extracted_text, img

def create_text(output_file_name, text):
    output_file_path = f"./Output_files/{output_file_name[:-4]}.txt"
    text_joined = ','.join(text)
    text_completion = text_joined[:-1]
    with open(output_file_path, 'w') as file2write:
        file2write.write(text_completion)
    print(f"Archivo txt para {output_file_name} generado con exito")
    return text_completion 

    
@app.route('/uploads',methods=['POST'])
def pos ():
    if 'file' not in request.files:
        return {
            "code":400,
            "msg":'No se ha proporcionado ningún archivo'
        } , 400
    
    file = request.files['file']
    
    if file.filename == '':
        return {
            "code":400,
            "msg":'No se ha seleccionado ningún archivo'
        } , 400

    if not file.filename.endswith('.pdf'):
        return {
            "code": 400,
            "msg": 'El archivo proporcionado no es un archivo PDF'
        }, 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        generated_files = pdf2png(filepath)
        reader = Reader()
        extracted_text_all = []
        for generated_file in generated_files:
            img = reader.read_img(generated_file)
            extracted_text, _ = reader(img)
            extracted_text_all.extend(extracted_text)

        output_text = create_text(filename, extracted_text_all)

        for generated_file in generated_files:
            os.remove(generated_file)
        os.remove(filepath)

        return jsonify({'texto_extraido': output_text})

    else:
        return jsonify({'error': 'Extensión de archivo no permitida'})

if __name__ == '__main__':
    app.run(debug=True)
