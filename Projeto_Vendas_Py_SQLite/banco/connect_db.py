import sqlite3


class VProduces():
    def __init__(self, banc):
        self.conn = sqlite3.connect(banc)
        self.curs = self.conn.cursor()


    def close_connect(self):
        self.curs.close()
        self.conn.close()

    def insert_into(self, nome_cliente, produto, peso, valor, data):
        try:
            action = "INSERT INTO vendas (nome_cliente, produto, peso, valor, data) VALUES (?, ?, ?, ?, ?)"

            self.curs.execute(action,(nome_cliente, produto, peso, float(valor), data))
            self.conn.commit()
        except Exception as error:
            print('Insert_into: ', error)

        self.close_connect()

    def update_table(self,name, valuer, validity, id):
        action = "UPDATE produtos SET name=?, value=?, validity=? WHERE id=?"
        self.curs.execute(action,(name, valuer, validity, id))
        self.conn.commit()

        self.close_connect()

    def delete_table(self,ident):
        action = "DELETE FROM produtos WHERE id=:id"
        self.curs.execute(action,{'id': ident})
        self.conn.commit()

        self.close_connect()


    # def select_from_tabela(self):
    #     self.curs.execute("SELECT * FROM produtos")
    #     values = self.curs.fetchall()
    #
    #
    #     self.close_connect()
    #
    # def select_from_tabela_where_name(self,name):
    #     self.curs.execute("SELECT * FROM produtos WHERE name LIKE :name",{'name': f'%{name}%'})
    #     values = self.curs.fetchall()
    #

        self.close_connect()

    def get_fruits(self):
        self.curs.execute("SELECT nome_produto, preco FROM produtos")
        values = self.curs.fetchall()

        self.close_connect()
        return values

    def get_clients(self):
        self.curs.execute("SELECT * FROM clientes")
        values = self.curs.fetchall()
        self.close_connect()
        return values

    def get_vendas(self):
        self.curs.execute("SELECT * FROM vendas")
        values = self.curs.fetchall()

        self.close_connect()
        return values

    def get_vendas_where_name_date(self, name, data=None):
        action = "SELECT * FROM vendas WHERE nome_cliente LIKE :nome AND data = :datas;"
        self.curs.execute(action,{'nome': f'%{name}%', 'datas': f"{data}"})
        values = self.curs.fetchall()

        self.close_connect()
        return values

    def get_vendas_where_name(self, name):
        action = "SELECT * FROM vendas WHERE nome_cliente LIKE :nome;"
        self.curs.execute(action,{'nome': f'%{name}%'})
        values = self.curs.fetchall()

        self.close_connect()
        return values

    def insert_client_into(self, nome_cliente, idade):
        try:
            action = "INSERT INTO clientes (nome_cliente, idade_cliente) VALUES (?, ?)"

            self.curs.execute(action,(nome_cliente, int(idade)))
            self.conn.commit()
        except Exception as error:
            print('Insert_into: ', error)

        self.close_connect()

    def update_cliente(self, name, idade, idr):
        print(name,idade,idr)
        action = "UPDATE clientes SET nome_cliente=:name, idade_cliente=:idade WHERE id_cliente=:idr"
        self.curs.execute(action, {"name": str(name), "idade": int(idade), "idr": int(idr)})
        self.conn.commit()

        self.close_connect()

    def delete_client(self,ident):
        action = "DELETE FROM clientes WHERE id_cliente=:id"
        self.curs.execute(action,{'id': ident})
        self.conn.commit()

        self.close_connect()


if __name__ == '__main__':
    buy = VProduces('vprodutos.db')
    print(buy.get_vendas_where_name('Junior'))

