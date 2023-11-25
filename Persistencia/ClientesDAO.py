from Beans import ClientesBean
from Persistencia import ClientesDAOListener
from Util.Conexao import *


class ClientesDAO(ClientesDAOListener):
    def __init__(self):
        try:
            self.conn = Conexao.getConnection()
        except Exception as e:
            raise Exception("Erro: " + ":\n" + str(e))

    def salvar(self, cliente: ClientesBean) -> None:
        cursor = None
        if cliente is None:
            raise Exception("O valor passado não pode ser nulo")

        try:
            SQL = "INSERT INTO Clientes (Nome, CPF_RG, Idade, Data_Nascimento, Endereco, Bairro, Cidade, Numero, Forma_PG, Valor) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
            cursor = self.conn.cursor()
            cursor.execute(SQL, cliente.getNome(), cliente.getCPF_RG(), cliente.getIdade(),
                           cliente.getData_Nascimento(), cliente.getEndereco(), cliente.getBairro(),
                           cliente.getCidade(), cliente.getNumero(), cliente.getForma_PG().getNome(),
                           cliente.getValor())
            self.conn.commit()
        except pyodbc.Error as e:
            raise Exception("Erro ao inserir dados " + str(e))
        finally:
            Conexao.closeConnection(cursor)

    def excluir(self, cliente: ClientesBean) -> None:
        cursor = None
        if cliente is None:
            raise Exception("O valor passado não pode ser nulo")

        try:
            SQL = "DELETE from Clientes where Nome=?"
            cursor = self.conn.cursor()
            cursor.execute(SQL, cliente.getNome())
            self.conn.commit()
        except pyodbc.Error as e:
            raise Exception("Erro ao excluir dados " + str(e))
        finally:
            Conexao.closeConnection(cursor)

    def atualizar(self, cliente: ClientesBean) -> None:
        cursor = None
        if cliente is None:
            raise Exception("O valor passado não pode ser nulo")

        try:
            SQL = "UPDATE Clientes SET Nome = ?, CPF_RG = ?, Idade = ?, Data_Nascimento = ?, Endereco = ?, Bairro = ?, Cidade = ?, Numero = ?, Forma_PG = ?, Valor = ?) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
            cursor = self.conn.cursor()
            cursor.execute(SQL, cliente.getNome(), cliente.getCPF_RG(), cliente.getIdade(),
                           cliente.getData_Nascimento(), cliente.getEndereco(), cliente.getBairro(),
                           cliente.getCidade(), cliente.getNumero(), cliente.getForma_PG().getNome(),
                           cliente.getValor())
            self.conn.commit()
        except pyodbc.Error as e:
            raise Exception("Erro ao inserir dados " + str(e))
        finally:
            Conexao.closeConnection(cursor)

    def todosClientes(self):
        Conexao.getConnection()
        cursor = self.conn.cursor()

        query = "SELECT * FROM Clientes"
        cursor.execute(query)

        list = []
        for row in cursor.fetchall():
            ID = row[0]
            Nome = row[1]
            cliente = self.ClientesBean(ID, Nome)
            list.append(cliente)

        Conexao.closeConnection(cursor)
        return list

    def todasFormasPagamento(self):
        Conexao.getConnection()
        cursor = self.conn.cursor()

        query = "SELECT * From FormasPagamento"
        cursor.execute(query)

        list = []
        for row in cursor.fetchall():
            ID = row[0]
            Nome = row[1]
            Forma_PG = self.FormasPagamentoBean(ID, Nome)
            list.append(Forma_PG)

        Conexao.closeConnection(cursor)
        return list

    def procurarCliente(self, Nome):
        Conexao.getConnection()
        cursor = self.conn.cursor()

        try:
            cursor.execute("SELECT * FROM cliente WHERE Nome=?", Nome)
            row = cursor.fetchone()

            if not row:
                raise Exception("Nenhum registro encontrado com o Nome: " + str(Nome))

            ID = row[1]
            Nome = row[2]
            Forma_PG = self.procurarFormasPagamento(row[3])

            return self.ClientesBean(ID, Nome, Forma_PG)

        except pyodbc.Error as e:
            raise Exception(e)

        finally:
            Conexao.closeConnection(cursor)

    def procurarFormasPagamento(self, ID):
        Conexao.getConnection()
        cursor = self.conn.cursor()

        try:
            cursor.execute("SELECT * FROM FormasPagamento WHERE ID=?", ID)
            row = cursor.fetchone()

            if not row:
                raise Exception("Nenhum registro encontrado com o ID: " + str(ID))

            ID = row[1]
            Nome = row[2]

            return self.FormasPagamentoBean(ID, Nome)

        except pyodbc.Error as e:
            raise Exception(e)

        finally:
            Conexao.closeConnection(cursor)
