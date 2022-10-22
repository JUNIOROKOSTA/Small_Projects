from pathlib import Path
import PyPDF2
import os

caminho = Path(__file__).parent
arquivo_pdf = caminho / 'pdf' / 'Overlord - Volume 01 - O Rei Undead.pdf'

with open('texto.txt', 'a', encoding='utf-8') as f:
    texto = PyPDF2.PdfReader(arquivo_pdf)
    textos = []
    for i in range(5, 10):
        page = texto.pages[i]
        if len(page.extract_text()) > 100:
            valor = (str(page.extract_text().replace('OVERLORD         1 O Rei Undead',
                ' ').replace('Capítulo          1 O Fim e o Começo', ' ')))
            
            textos.append(valor)
    for t in textos:
        f.write(t.replace('\n', ''))
        f.write('\n')
        
