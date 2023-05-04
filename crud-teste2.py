# Criar dados ao banco de dados


import mysql.connector

try:
    #Criar conexão ao banco de dados
    con = mysql.connector.connect(
        host = 'localhost',
        database = 'cadastro',
        user = 'root',
        password= ''
    )

    #Declaração sql a ser executada
    nova_tabela = """ CREATE TABLE produtos ( id int not null auto_increment, nomeProduto varchar(70) NOT NULL, preco float NOT NULL, quantidade TINYINT NOT NULL, PRIMARY KEY (id))"""

    #Criar cursor e executar SQL no banco de dados
    cursor = con.cursor()
    cursor.execute(nova_tabela)
    print("Tabela criada com sucesso!")
except mysql.connector.Error as erro:
    print("Falha ao criar tabela no MySQL: {}".format(erro))
finally:
    if(con.is_connected()):
        cursor.close()
        con.close()
        print("Conexão ao MySQL finalizada!")


#Falta colocar pra rodar
#Parei em 1:33 min