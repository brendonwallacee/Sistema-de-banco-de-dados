from Util.Modulos import *
from Beans import ClientesBean
from Beans import FormasPagamentoBean
from typing import List

class ClientesDAOListener:
    def atualizar(self, cliente: ClientesBean) -> None:
        pass

    def excluir(self, cliente: ClientesBean) -> None:
        pass

    def procurarCliente(self, Nome: str) -> ClientesBean:
        pass

    def salvar(self, cliente: ClientesBean) -> None:
        pass

    def todosClientes(self, cliente: ClientesBean) -> List:
        pass

    def todasFormasPagamento(self, Forma_PG: FormasPagamentoBean) -> List:
        pass
