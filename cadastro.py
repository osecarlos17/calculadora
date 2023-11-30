import os

import mysql.connector

Conectar = mysql.connector. connect(host='localhost',
                                    database='cadastro',
                                    user='jose',
                                    password='123456')

print('Deseja ver cadastrado ou se cadastra? ver cadastardo (1) se cadastra (2) sair do programa (3):')
vercadastardo= 1
secadastra= 2
sairdoprograma = 3

cadastra = input ()
if cadastra == "2":
    print('Nome:')
    nome =  input()
    print('email:')
    email = input ()
    print('genero:')
    genero= input()
    print('Cpf:')
    Cpf = input()   
    print('telefone:')  
    telefone = input ()
    print('Motos:')
    Motos = input ()
    print ('cadastrado com sucesso!')


if Conectar.is_connected():
    print('Conexão realizado com sucesso')
else:
    print('falha na conexão')


ComandoSelect = 'SELECT *  FROM tb_cadastro;'

cursor = Conectar.cursor()
cursor.execute(ComandoSelect)
retornoDeDados = cursor.fetchall()


cursor.close()
print('conexão finalizada!')

print('Forma01')
print(retornoDeDados)

cursor.close()
print('Conexão finalizada')

if cadastra == "1":
    comandoinsert = """inset into  ( nome, email, genero, Cpf, telefone, Motos ) values ('Sarah', 'sarahramos@gmail.com', 'F', '18219822821',
 '9410-0283 ' , 'pop');""" 


    comandoinsert = """insert into tb_cadastro  ( nome, email, genero, Cpf, telefone, Motos ) values  ('Samuel', 'samuelrocha2@gmail.com', 'M', '03360457862',
    '(85) 98507-7578 ' , 'pop', '0009871' );""" 

    os.system('cls')
    comandoinsert = """insert into tb_cadastro  ( nome, email, genero, Cpf, telefone, Motos) values ('klaide', 'klaidedelisia@gmail.com', 'F','15334162496'  
    '96912-3016','pop');"""

    os.system('cls')
    comandoinsert = """insert into tb_cadastro  ( nome, email, genero, Cpf, telefone, Motos) values ('maisa', 'maisaclara2@gamil.com', 'F', '23432145632',
    '9531-1783', 'XRE300');"""

    os.system('cls')

else:
 cadastra == '3'
 print('Finalizado!')



    

for i in retornoDeDados:
    print('_____')
    for x in i:
        print(x)



