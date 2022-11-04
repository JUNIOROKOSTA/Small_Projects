import requests
import json


class WebReq():
    def __init__(self):
        self.api_ultimo = 'https://loteriascaixa-api.herokuapp.com/api/mega-sena/latest'
        self.api_concurso = 'https://loteriascaixa-api.herokuapp.com/api/mega-sena/'

    def ultimo_concurso(self):
        ult_concurso = self.api_ultimo
        ult_concurso = requests.get(ult_concurso)
        ult_concurso_json = ult_concurso.json()

        prox_c = ult_concurso_json['proxConcurso']
        data_prox_c = ult_concurso_json['dataProxConcurso']
        valor_premio = ult_concurso_json['premiacoes'][0]['premio']

        return prox_c, data_prox_c, valor_premio

    def consultar_concurso(self, num):
        num = int(num)
        concurso = f'{self.api_concurso}{num}'
        concurso = requests.get(concurso)
        concurso_json = concurso.json()

        dezenas = concurso_json['dezenas']
        premiacoes = concurso_json['premiacoes'][0]['premio']

        return dezenas, premiacoes
