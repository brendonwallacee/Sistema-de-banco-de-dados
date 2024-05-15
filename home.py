from tkinter import *
from tkinter import ttk
from Persistencia import ClientesDAO
 

root = Tk()

class Application():
    def __init__(self):
        self.root=root
        self.root.title("OptoSystem")
        self.root.geometry('1080x720')
        self.menus()
        
        self.root.mainloop()

    def menus(self):
        menubar = Menu(self.root)
        
        clientes = Menu(menubar, tearoff=0)
        clientes.add_command(label="Novo Cliente", command=self.add_cliente)
        clientes.add_command(label="Procurar Clientes")
        clientes.add_command(label="Excluir Cliente")

        menubar.add_cascade(label="Clientes", menu=clientes)


        receitas = Menu(menubar, tearoff=0)
        receitas.add_command(label="Nova Receita", command=self.faz_nada)
        receitas.add_command(label="Procurar Receitas")
        receitas.add_command(label="Excluir Receita")

        menubar.add_cascade(label="Receitas", menu=receitas)


        financeiro = Menu(menubar, tearoff=0)
        financeiro.add_command(label="Movimentação Diária")
        financeiro.add_command(label="Consultar Financeiro", command=self.faz_nada)
        financeiro.add_command(label="Formas de Pagamento")


        menubar.add_cascade(label="Finança", menu=financeiro)
        self.root.config(menu=menubar)
                         
    def frames(self): 
        self.frame1()
        self.frame2()
        
    def frame1(self):
        self.frm1 = ttk.Frame(self.direct, padding=40)
        self.frm1.pack(side=LEFT)
        self.lnome = Label(self.frm1, text="Qual o medicamento que irá utilizar?")
        self.lnome.grid(column=0, row=1)
        self.tfnome = Entry(self.frm1, width=50)
        self.tfnome.grid(column=0, row=2)
        self.ltipo = Label(self.frm1, text="Qual o tipo de remedio?")
        self.ltipo.grid(column=0, row=3)
        self.tftipo = Entry(self.frm1, width=50)
        self.tftipo.grid(column=0, row=4)
        self.ldias = Label(self.frm1, text="Por quantos dias deverá tomar?")
        self.ldias.grid(column=0, row=5)
        self.tfdias = Entry(self.frm1, width=50)
        self.tfdias.grid(column=0, row=6)
        self.ltempo = Label(self.frm1, text="De quantas em quantas horas deverá tomar?")
        self.ltempo.grid(column=0, row=7)
        self.tftempo = Entry(self.frm1, width=50)
        self.tftempo.grid(column=0, row=8)

    def frame2(self):
        self.frm2 = ttk.Frame(self.direct, padding=40)
        self.frm2.pack(side=LEFT)
        btreg = Button(self.frm2, text="Salvar", command=self.registro, width=20, height=2, borderwidth=2)
        btreg.grid(column=0, row=1, padx=10, pady=5)

        btalarm = Button(self.frm2, text="Registrar Alarme", command=self.alarme, width=20, height=2)
        btalarm.grid(column=0, row=2, padx=10, pady=5)

        saia = Button(self.frm2, text="Sair", command=self.root.destroy, width=20, height=2)
        saia.grid(column=0, row=3, padx=10, pady=5)

        mostra = Button(self.frm2, text="Mostrar Entrada", command=self.entrada, width=20, height=2, borderwidth=2)
        mostra.grid(column=0, row=4, padx=10, pady=5)
    
    def add_cliente(self):
        self.direct = Toplevel(self.root)
        self.frames()

    def faz_nada(self):
        pass

    def registro(self):
        self.nome = str(self.tfnome.get())
        self.tipo = str(self.tftipo.get())
        self.dias = int(self.tfdias.get())
        self.tempo = int(self.tftempo.get())

    def entrada(self):
        self.janela1 = Tk()
        self.janela1.title("Dados do remédio")
        self.janela1.geometry('550x50')

        self.nome = str(self.tfnome.get())
        self.tipo = str(self.tftipo.get())
        self.dias = int(self.tfdias.get())
        self.tempo = int(self.tftempo.get())

        self.lremedio1 = Label(self.janela1, text=str("sla"))
        self.lremedio1.pack(side=LEFT, padx=20)
        self.voltar1 = Button(self.janela1, text="Voltar", command=self.janela1.destroy)
        self.voltar1.pack(side=RIGHT, padx=20)


    def alarme(self):
        self.nome = str(self.tfnome.get())
        self.tipo = str(self.tftipo.get())
        self.dias = int(self.tfdias.get())
        self.tempo = int(self.tftempo.get())
    
    


Application()