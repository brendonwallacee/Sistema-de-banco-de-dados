import pyodbc

class Conexao:
    def _init_(self):
        pass

    # Criação da função para abrir conexão com o BD SQL Server
    @staticmethod
    def getConnection():
        try:
            conn = 'DRIVER={SQL Server};SERVER=LAPTOP-BJQUB3C4\BD_CEOOP;DATABASE=CEOOP;'
            return pyodbc.connect(conn)
        except Exception as e:
            raise Exception(str(e))

    # Criação da função para fechar conexão com o BD SQL Server
    @staticmethod
    def closeConnection(conn, stmt=None, rs=None):
        try:
            if rs:
                rs.close()
            if stmt:
                stmt.close()
            if conn:
                conn.close()
        except Exception as e:
            raise Exception(str(e))
