from pathlib import Path
from tradutor_google import tradutor_texto
import cv2
import os
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def extracty_texto(imgs, count):
    img = cv2.imread(imgs)
    texto = pytesseract.image_to_string(img, lang='por')
    texto = tradutor_texto(texto)
    with open('texto_extract.txt', 'a', encoding='utf-8') as f:
        f.write('#'*30)
        f.write(f'\n -----> Imagem {count} <------ \n')
        f.write(f'{texto} \n')


count = 1
caminho = Path(__file__).parent
caminho = caminho / 'img'

for root, dirs, files in os.walk(caminho):
    for file in files:
        imagem = os.path.join(root, file)
        extracty_texto(imagem, count)
        count += 1
