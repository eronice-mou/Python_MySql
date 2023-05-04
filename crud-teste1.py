# Inserir dados na tabela


import mysql.connector
from mysql.connector import Error

#Inserindo registros em um banco de dados MySQL

try:
    con = mysql.connector.connect(
        host = 'localhost',
        database = 'cadastro',
        user = 'root',
        password= ''
        
    )
    
    inserir_produtos = """INSERT INTO pessoas(nome, nascimento, sexo, peso, altura, nacionalidade) VALUES ('André Souza', '1987-03-21', 'M', '94', '1.80', 'Brasileiro')"""

    cursor = con.cursor()
    cursor.execute(inserir_produtos)
    con.commit()
    print(cursor.rowcount, "registros inserodos na tabela!")
    cursor.close()
except Error as erro:
    print("Falha ao inserir dados no MySQL: {}".format(erro))
finally:
    if (con.is_connected()):
        con.close()
        print("Conexão ao MySQL finalizada")
