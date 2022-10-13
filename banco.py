import sqlite3
from sqlite3 import Error
import os

pastaApp = os.path.dirname(__file__) # Indicar em qual pasta esta o arquivo
nomeBanco = pastaApp+"\\contatos.db" # Indicar o DB que será aberto

def ConexaoBanco():
    con = None # Zerar a variável "con"
    try:
        con = sqlite3.connect(nomeBanco) # Gerar a variável de conexao com o DB
    except Error as ex:
        print(ex) # Caso apresente um erro, printar o mesmo
    return con # Retornar a variável "con" que seria a conexao com o DB

def dql(query): # COMANDO SELECT
    """Usar para comando de SELECT (Pesquisar)"""
    vcon = ConexaoBanco() # Vcon será a conexao com o DB
    cursor = vcon.cursor() # criar um cursor para dar os comandos
    cursor.execute(query) # Executar o comando passado pelo parâmetro "query"
    res=cursor.fetchall() # Comando fetchall coleta as infos que apareceram após a busca no DB
    vcon.close() # Fechar a conexão com o DB
    return res # Retornar como resultado da função as linhas encontradas

def dml(query): # COMANDO INSERT, UPDATE, DELETE
    """Usar para comando de INSERT, UPDATE E DELETE (Inserir, Atualizar e Deletar)"""
    try:
        vcon = ConexaoBanco() # Vcon será a conexao com o DB
        cursor = vcon.cursor() # criar um cursor para dar os comandos
        cursor.execute(query) # Executar o comando passado pelo parâmetro "query"
        vcon.commit() # Realizar o Commit (confirmação do que foi alterado) no DB
        vcon.close() # Fechar conexão com o DB
    except Error as ex:
        print(ex) # Caso dê errado, printar o erro

def criarBanco():
    conn = sqlite3.connect(nomeBanco) # Criar/Conectar um DB com o nome de "agenda"

    cursor = conn.cursor() # Criar um cursor dentro do DB

    cursor.execute("""CREATE TABLE IF NOT EXISTS tb_nomes (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
    nome VARCHAR(50), 
    fone VARCHAR(14))""")