"""
Versão que funciona
pip install googletrans==3.1.0a0
"""

from googletrans import Translator


def tradutor_texto(texto):
    tradutor = Translator()
    msn = tradutor.translate(texto, 'pt')
    return msn.text
