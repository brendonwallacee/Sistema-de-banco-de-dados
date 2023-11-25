from typing import List
from Beans.ClientesBean import ClientesBean
from Beans.FormasPagamentoBean import FormasPagamentoBean

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
