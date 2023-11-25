class ClientesBean:

    # Método Construtor e criação dos métodos get e set para os atributos
    def __init__(self, ID, Nome, CPF_RG, Idade, Data_Nascimento, Endereco, Bairro, Cidade, Numero, Forma_PG, Valor):
        self._ID = ID
        self._Nome = Nome
        self._CPF_RG = CPF_RG
        self._Idade = Idade
        self._Data_Nascimento = Data_Nascimento
        self._Endereco = Endereco
        self._Bairro = Bairro
        self._Cidade = Cidade
        self._Numero = Numero
        self._Forma_PG = Forma_PG
        self._Valor = Valor

    def ClientesBean(self, ID, Nome):
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

    def getCPF_RG(self):
        return self._CPF_RG

    def setCPF_RH(self, CPF_RG):
        self._CPF_RG = CPF_RG

    def getIdade(self):
        return self._Idade

    def setIdade(self, Idade):
        self._Idade = Idade

    def getData_Nascimento(self):
        return self._Data_Nascimento

    def setData_Nascimento(self, Data_Nascimento):
        self._Data_Nascimento = Data_Nascimento

    def getEndereco(self):
        return self._Endereco

    def setEndereco(self, Endereco):
        self._Endereco = Endereco

    def getBairro(self):
        return self._Bairro

    def setBairro(self, Bairro):
        self._Bairro = Bairro

    def getCidade(self):
        return self._Cidade

    def setCidade(self, Cidade):
        self._Cidade = Cidade

    def getNumero(self):
        return self._Numero

    def setNumero(self, Numero):
        self._Numero = Numero

    def getForma_PG(self):
        return self._Forma_PG

    def setForma_PG(self, Forma_PG):
        self._Forma_PG = Forma_PG

    def getValor(self):
        return self._Valor

    def setValor(self, Valor):
        self._Valor = Valor

    def __str__(self):
        return self._Nome

    # Criando um hash considerando os parâmetros do atributo "_nome"
    def __hash__(self):
        return hash(self._Nome)

    # Comparando um objeto já existente com o que foi passado dentro do parâmetro
    def __eq__(self, other):
        if self is other:
            return True
        if other is None or self.__class__ != other.__class__:
            return False
        if self._Nome != other.getNome():
            return False
        return True
