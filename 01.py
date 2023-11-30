import mysql.connector
Conectar = mysql.connector. connect(host='localhost',
                                    database='cadastro',
                                    user='jose',
                                    password='123456')

if Conectar.is_connected():
    print('Conexão realizado com sucesso')
else:
    print('falha na conexão')

Comandoinsert = " " "insert into tb_pessoa (Nome, Email, genero) values ('Bruno', 'brunoramos@gmail.com','M'); " " "

#Concatenação do Comando  

#sql = Comando_Insert + dados 

# Execução do Camando

cursor = Conectar.cursor()
cursor.execute(Comandoinsert)
Conectar.commit()
print('Salvo com sucesso')

cursor.close()
print('Conexão finalizada!')



