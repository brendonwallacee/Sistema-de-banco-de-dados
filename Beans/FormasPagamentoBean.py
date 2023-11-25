class FormasPagamentoBean:

    # Método Construtor e criação dos métodos get e set para os atributos
    def __init__(self, ID, Nome):
        self._ID = ID
        self._Nome = Nome

    def getID(self):
        return self._ID

    def setID(self, ID):
        self._ID = ID

    def getNome(self):
        return self._Nome

    def setNome(self, Nome):
        self._Nome = Nome

    def __str__(self):
        return self._Nome

    # Criando um hash considerando os valores do atributo "_Nome" e "_ID"
    def __hash__(self):
        return hash((self._Nome, self._ID))

    # Comparando um objeto já existente com o que foi passado dentro do parâmetro
    def __eq__(self, other):
        if self is other:
            return True
        if other is None or self.__class__ != other.__class__:
            return False
        if self._Nome != other.getNome() or self._ID != other.getID():
            return False
        return True
