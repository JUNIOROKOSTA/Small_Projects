import sqlite3


class Request_DB():
    def __init__(self, banc):
        self.conn = sqlite3.connect(banc)
        self.curs = self.conn.cursor()

    def close_connect(self):
        self.curs.close()
        self.conn.close()

    def insert_into(self, concurso, aposta, data):
        try:
            action = "INSERT INTO apostas (concurso, aposta, data_aposta) VALUES (?, ?, ?)"

            self.curs.execute(action, (concurso, aposta, data))
            self.conn.commit()
            self.close_connect()

        except Exception as error:
            self.close_connect()
            print('Insert_into: ', error)

    def update_table(self, resultado, valor_premio, acertos, concurso, aposta):
        try:
            action = "UPDATE apostas SET resultado=?, valor_premio=?, acertos=? WHERE concurso=? AND aposta=?"
            self.curs.execute(
                action, (resultado, valor_premio, acertos, concurso, aposta))
            self.conn.commit()
            self.close_connect()

        except Exception as error:
            self.close_connect()
            print('update_table: ', error)

    def get_apostas(self):
        action = "SELECT concurso, aposta,data_aposta,resultado,valor_premio,acertos FROM apostas"
        self.curs.execute(action)
        values = self.curs.fetchall()

        self.close_connect()
        return values

    def verific_aposta(self, concurso, aposta):
        action = "SELECT concurso, aposta FROM apostas WHERE concurso=:concurso AND aposta=:aposta"
        self.curs.execute(
            action, {'concurso': f'{concurso}', 'aposta': f'{aposta}'})
        values = self.curs.fetchall()
        if values:
            self.close_connect()
            return True

        self.close_connect()
        return False


if __name__ == '__main__':
    requisi = Request_DB('registros_db.db')

    concuso = '2022'
    aposta = '04-28-45-48-52-60'
    data = '14/03/2018'

    aposta_c = '04-28-45-48-52-60'
    valor = 'R$ 60.000.000,00'
    acertos = '6'

    # requisi.insert_into(concuso, aposta, data)
    # requisi.update_table(aposta_c, valor, acertos, concuso)

    print(requisi.verific_apostas(concurso=concuso, aposta=aposta))
