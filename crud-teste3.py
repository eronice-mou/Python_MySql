# Atualização de registro no banco de dados

import mysql.connector
from mysql.connector import Error


# função pra conectar ao banco de dados
def conectar():
    try:
        global con
        con = mysql.connector.connect(
            host = 'localhost',
            database = 'cadastro',
            user = 'root',
            password= ''    
        )
    except Error as erro:
        print("Erro de conexão")


#Função para consultar o banco de dados
def consulta(idPess):       
    try:
        conectar()
        consulta_sql = 'select * from pessoas WHERE Id = ' +idPess
        cursor = con.cursor()
        cursor.execute(consulta_sql)
        linhas = cursor.fetchall()

        for linha in linhas:
            print("Id: ", linha[0])
            print("Nome: ", linha[1])
            print("Nascimento: ", linha[2])
    except Error as erro:
        print("Falha ao consultar a tabela: {}".format(erro))
    finally:
        if(con.is_connected()):
            cursor.close()
            con.close()


#Função para atualizar o banco de dados
def atualiza(declaracao):
    try:
        conectar()
        altera_peso = declaracao
        cursor = con.cursor()
        cursor.execute(altera_peso)
        con.commit()
        print("Peso alterado com sucesso!")
    except Error as erro:
        print("Falha ao inserir dados na tabela: {}".format(erro))
    finally:
        if(con.is_connected()):
            cursor.close()
            con.close()

if __name__=='__main__':
    print("Atualizar o nome da pessoa no banco de dados")
    print("Entre com os dados conforme solicitado: ")

    #print("\nDigite o nome")
    idPess = input("Id do produto: ")

    consulta(idPess)

    print("\nEntre com o novo nome: ")
    nomePess = input("Nome: ")

    declaracao = """ UPDATE pessoas 
    SET Nome = """ + nomePess + """ 
    WHERE Id = """ + idPess

    print(declaracao)

    atualiza(declaracao)


