import conexao



Conectar = mysql.connector.connect(nome = 'Nome:',
                                    email = 'email',
                                    Genero = 'f',
                                    Cpf  =   'Cpf',
                                    Motos = 'Motos')


ComandoSelect = 'SELECT * FROM tb_cadastro ;'

cursor = Conectar.cursor()
cursor.execute(ComandoSelect)
retornoDeDados = cursor.fetchall()


 
conectar= Conexao.conectar

if conectar.is_connected():
    print('Cadastro Realizado com sucesso !')
else:
    print('Falha na conexão')

#varriaves de inserir valores 

nome = input ('Nome:')
email = input ('email')
Genero = input ('Genero ')
Cpf =  input ('Cpf')
Motos = input('Motos')

