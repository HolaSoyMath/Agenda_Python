from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import banco
import os

banco.criarBanco()

def popular():
    tv.delete(*tv.get_children()) # Deletar todos os registros que estão previamente no Treeview, apenas para ter certeza que veremos as informações zeradas
    vquery = "SELECT * FROM tb_nomes order by ID"
    linhas = banco.dql(vquery)
    for i in linhas:
        tv.insert("","end", values=i)

def inserir():
    # Verificar se há alguma variável que está vazia
    if vnome.get() == "" or vfone.get() == "":
        messagebox.showinfo(title="ERRO", message="Digite todos os dados")
        return
    try:
        # Gerar o comando SQL
        vquery = "INSERT INTO tb_nomes (nome, fone) VALUES ('"+vnome.get()+"','"+vfone.get()+"')"
        # Chamar a função do arquivo Banco que executa a Inserção de itens 
        banco.dml(vquery)
    except:
        # Avisar ao usuário que teve erro ao inserir a informação no DB
        messagebox.showinfo(title="ERRO", message="Erro ao inserir")
        return
    # Chamar a função Popular para "resetar" o treeview
    popular()
    # Deletar os dados digitados nos campos
    vnome.delete(0, END)
    vfone.delete(0, END)
    vnome.focus()

def remover():
    # Alocar em uma variavel os itens que foram selecionados
    itemSelecionado=tv.selection()
    for item in range(len(itemSelecionado)):
        # Verificar qual o ID selecionado
        vlr = tv.item(itemSelecionado[item], 'values')
        vquery = "DELETE FROM tb_nomes WHERE id = '{}'".format(vlr[0])
        banco.dml(vquery)
        popular()

def pesquisar():
    # Apagar todos os dados do Treeview
    tv.delete(*tv.get_children())
    # Gerar comando SQL apra consulta no Treeview
    vquery="SELECT * FROM tb_nomes WHERE nome LIKE '%"+vnomePesquisar.get()+"%' order by ID"
    # Gerar todas as linhas de pesquisa
    linhas=banco.dql(vquery)
    for i in linhas:
        # Inserir cada valor no Treeview
        tv.insert("", "end", values=i)
    

app=Tk()
app.title("Agenda")
app.geometry("600x450")

# Adicionar Icone na janela do aplicativo
pasta = os.path.dirname(__file__) # Indicar em qual pasta esta o arquivo
nomeicon = pasta+"\\agenda.png" # Indicar o DB que será aberto
icon = PhotoImage(file=nomeicon)
app.iconphoto(False, icon)

##### Criação de Frame do Treeview
### Criar o Frame
quadroTreeView = LabelFrame(app, text="Contatos")
# Posicionar o frame
quadroTreeView.pack(fill="both", expand="yes", padx=10, pady=10)

### Setar as colunas que aparecerão
tv=ttk.Treeview(quadroTreeView, columns=('id', 'nome', 'fone'), show='headings')
### Setar o tamanho das colunas
# id
tv.column('id', minwidth=0, width=50)
# nome
tv.column('nome', minwidth=0, width=250)
# fone
tv.column('fone', minwidth=0, width=100)

### Setar os nomes que aparecerão nas colunas
# ID
tv.heading('id', text='ID')
# NOME
tv.heading('nome', text='NOME')
# TELEFONE
tv.heading('fone', text='TELEFONE')

### Posicionar o Treeview
tv.pack()

### Função para preencher os dados do DB para o Treeview
popular()

##### Criação do Frame de inserir dados no DB
# Criar o Frame
quadroInserir = LabelFrame(app, text="Inserir Novos Contatos")
# Posicionar o Frame
quadroInserir.pack(fill="both", expand="yes", padx=10, pady=10)

##### Criar campos que aparecerão dentro do frame de "inserir"
### Campos NOME
# Criar Label 
lbnome=Label(quadroInserir, text="Nome")
lbnome.pack(side="left")

# Criar Inputbox
vnome = Entry(quadroInserir)
vnome.pack(side="left", padx=10)

### Campos TELEFONE
# Criar Label
lbfone=Label(quadroInserir, text="Fone")
lbfone.pack(side="left")

# Criar inputbox
vfone=Entry(quadroInserir)
vfone.pack(side="left", padx=10)

### Botão de inserir nome
# Criar botao para ação
btn_inserir=Button(quadroInserir, text="Inserir", command=inserir)
btn_inserir.pack(side="left", padx=10)

##### Criação do Frame de PESQUISAR dados no DB
# Criar o Frame
quadroPesquisar=LabelFrame(app, text="Pesquisar/Remover Contatos")
quadroPesquisar.pack(fill="both", expand="yes", padx=10, pady=10)

### Pesquisa de NOME
# Criar Label
lbid=Label(quadroPesquisar, text="Nome")
lbid.pack(side="left")

# Criar inputbox
vnomePesquisar = Entry(quadroPesquisar)
vnomePesquisar.pack(side="left")

### Botões de pesquisa
# Pesquisa unitária
btn_pesquisar=Button(quadroPesquisar, text="Pesquisar", command=pesquisar)
btn_pesquisar.pack(side="left", padx=10)

# Mostrar todos os itens
btn_todos=Button(quadroPesquisar, text="Mostrar todos", command=popular)
btn_todos.pack(side="left", padx=10)

### Botão de remover
# Remover itens selecionados
btn_remover=Button(quadroPesquisar, text="Remover", command=remover)
btn_remover.pack(side="left", padx=10)

app.mainloop()