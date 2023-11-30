import mysql.connector

Conectar = mysql.connector. connect(host='localhost',
                                    database='cadastro',
                                    user='jose',
                                    password='123456')

if Conectar.is_connected():
    print('Conexão realizado com sucesso')
else:
    print('falha na conexão')

ComandoSelect = 'SELECT * FROM tb_pessoa;'

cursor = Conectar.cursor()
cursor.execute(ComandoSelect)
retornoDeDados = cursor.fetchall()


print('Forma01')
print(retornoDeDados)

cursor.close()
print('Conexão finalizada')

for i in retornoDeDados:
    print (i)

for i in retornoDeDados:
    print('_____')
    for x in i:
        print(x)
        