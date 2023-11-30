import os
os.system('cls')
import re
regra = re.compile(r"(0|-?[1-9][0-9]*)")

def calculo_desconto(a):
   if a<=1212:
      Salario_atualizado=a-((a*7.5)/100) 
      return Salario_atualizado
   if 1212.01<a<=2427.35:
      Salario_atualizado=a-((a*9)/100)
      return Salario_atualizado
   if 2427.36<a<=3641.03:
      Salario_atualizado=a-((a*12)/100)
      return Salario_atualizado
   if 3641.04<a<=7087.22 or a > 7087.22:
      Salario_atualizado=a-((a*14)/100)
      return Salario_atualizado


print('Sistema do Calculo de Contracheque de Funcionários')

while True:
   Nome = input("Qual seu nome?:")
   if regra.match(Nome):
      os.system('cls')
      print('Nesse campo so pode usar letras')
      
   else:
      break   
#Validar apenas letras no campo nome
#---------------------------------------------------------------------


while True:
   try:
      Salario = float(input("Qual o seu salário?:"))
      Salario_com_desconto = calculo_desconto (Salario)
      break
   except ValueError:
      os.system('cls')
      print('Nesse campo so pode usar números')
#Validar apenas números no campo salário
#---------------------------------------------------------------------
   







while True:
   try:
      Hora_extra = float(input('Quanto você fez de hora extra?:'))
      break
   except ValueError:
      os.system('cls')
      print('Nesse campo so pode usar números')
# Validar apenas números no campo hora extra
#---------------------------------------------------------------------


Setor = input('Qual o seu setor? (operacional ou adm):')
while Setor != 'operacional' or Setor != 'adm':
   if Setor == 'operacional' or Setor == 'adm':
      break
   else:
      os.system('cls')
      print('Setor não identificado! Digite novamente->')
      Setor = input('Qual o seu setor? (operacional ou adm):')
#Validar o setor
#---------------------------------------------------------------------

os.system('cls')

if Setor == 'adm':
   Valor_da_hora_extra = 4.50
else:
   Valor_da_hora_extra = 3.50
#Dar valor a hora extra a partir do setor
#---------------------------------------------------------------------

if Hora_extra <=4:
   Salario_calculado = Salario + (Hora_extra * Valor_da_hora_extra)
   banco_de_hora = 0
else:
   Salario_calculado= Salario + (4 * Valor_da_hora_extra)
   banco_de_hora= (Hora_extra - 4)
   banco_de_hora=round(banco_de_hora,3)
#Cálculo do salário e horas extras
#---------------------------------------------------------------------

banco_de_hora_minutos = banco_de_hora * 60
#Cálculo para transformar horas em minutos
#---------------------------------------------------------------------

if banco_de_hora > 0:
 print('ContraCheque Finalizado Com Sucesso!')
 print('NOME DO FUNCIONÁRIO:', Nome)
 print('SALÁRIO ATUALIZADO:',Salario_calculado, 'reais')
 print('SALARIO_COM_DESCONTO',Salario_com_desconto)
 print('BANCO DE HORAS:', banco_de_hora, 'horas ou',banco_de_hora_minutos,'minutos')
 print('Sistema Finalizado!')
else:
 print('ContraCheque Finalizado Com Sucesso!')
 print('NOME DO FUNCIONÁRIO:', Nome)
 print('SALÁRIO ATUALIZADO:', Salario_calculado, 'reais')
 print('SALARIO_COM_DESCONTO',Salario_com_desconto)
 print('BANCO DE HORAS:', banco_de_hora, 'horas')
 print('Sistema Finalizado!')
