from tkinter import *
from tkinter.ttk import *
import customtkinter
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
                         
    def cliente_frames(self): 
        self.entradas_clientes()
        # self.botoes_clientes()
        
    def entradas_clientes(self):
        frm1 = Frame(self.direct, padding=5)
        frm1.grid(column=1, row=1)
        frm2 = Frame(self.direct, padding=5)
        frm2.grid(column=1, row=2)
        frm3 = Frame(self.direct, padding=5)
        frm3.grid(column=1, row=3)
        frm4 = Frame(self.direct, padding=5)
        frm4.grid(column=1, row=4)
        self.lnome = Label(frm1, text="Nome:")
        self.lnome.pack(side=LEFT)
        self.tfnome = Entry(frm1, width=58)
        self.tfnome.pack(side=LEFT)
        self.ldias = Label(frm2, text="CPF ou RG:")
        self.ldias.pack(side=LEFT)
        self.tfdias = Entry(frm2, width=14)
        self.tfdias.pack(side=LEFT)
        self.ltipo = Label(frm2, text="Idade:")
        self.ltipo.pack(side=LEFT)
        self.tftipo = Entry(frm2, width=3)
        self.tftipo.pack(side=LEFT)
        self.ltempo = Label(frm2, text="Data de Nascimento:")
        self.ltempo.pack(side=LEFT)
        self.tftempo = Entry(frm2, width=10)
        self.tftempo.pack(side=LEFT)
        self.ltempo = Label(frm3, text="Endereço:")
        self.ltempo.pack(side=LEFT)
        self.tftempo = Entry(frm3, width=55)
        self.tftempo.pack(side=LEFT)
        self.ltempo = Label(frm4, text="Bairro:")
        self.ltempo.pack(side=LEFT)
        self.tftempo = Entry(frm4, width=23)
        self.tftempo.pack(side=LEFT)
        self.ltempo = Label(frm4, text="Cidade:")
        self.ltempo.pack(side=LEFT)
        self.tftempo = Entry(frm4, width=27)
        self.tftempo.pack(side=LEFT)

    def botoes_clientes(self):
        self.frm2 = Frame(self.direct, padding=40)
        self.frm2.pack(side=BOTTOM)
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
        self.direct.title("Novo Cliente")
        self.direct.focus_force()
        self.cliente_frames()

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