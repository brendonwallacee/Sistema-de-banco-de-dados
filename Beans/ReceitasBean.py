class ReceitasBean:
    def __init__(self, ID_RX, Nome_Cliente, Data_Exame, OD_Esf, OE_Esf, OD_Cil, OE_Cil, OD_Ax, OE_Ax, Ad, Obs):
        self._ID_RX = ID_RX
        self._Nome_Cliente = Nome_Cliente
        self._Data_Exame = Data_Exame
        self._OD_Esf = OD_Esf
        self._OE_Esf = OE_Esf
        self._OD_Cil = OD_Cil
        self._OE_Cil = OE_Cil
        self._OD_Ax = OD_Ax
        self._OE_Ax = OE_Ax
        self._Ad = Ad
        self._Obs = Obs

    def getID_RX(self):
        return self._ID_RX

    def setID_RX(self, ID_RX):
        self._ID_RX = ID_RX

    def getNome_Cliente(self):
        return self._Nome_Cliente

    def setNome_Cliente(self, Nome_Cliente):
        self._Nome_Cliente = Nome_Cliente

    def getData_Exame(self):
        return self._Data_Exame

    def setData_Exame(self, Data_Exame):
        self._Data_Exame = Data_Exame

    def getOD_Esf(self):
        return self._OD_Esf

    def setOD_Esf(self, OD_Esf):
        self._OD_Esf = OD_Esf

    def getOD_Cil(self):
        return self._OD_Cil

    def setOD_Cil(self, OD_Cil):
        self._OD_Cil = OD_Cil

    def getOD_Ax(self):
        return self._OD_Ax

    def setOD_Ax(self, OD_Ax):
        self._OD_Ax = OD_Ax

    def getOE_Esf(self):
        return self._OE_Esf

    def setOE_Esf(self, OE_Esf):
        self._OE_Esf = OE_Esf

    def getOE_Cil(self):
        return self._OE_Cil

    def setOE_Cil(self, OE_Cil):
        self._OE_Cil = OE_Cil

    def getOE_Ax(self):
        return self._OE_Ax

    def setOE_Ax(self, OE_Ax):
        self._OE_Ax = OE_Ax

    def getAd(self):
        return self._Ad

    def setAd(self, Ad):
        self._Ad = Ad

    def getObs(self):
        return self._Obs

    def setObs(self, Obs):
        self._Obs = Obs
