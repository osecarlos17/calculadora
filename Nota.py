print('Seja bem vindo a nota do seu filho')
print('Nota')

while True:
   Nome = input("Nome:")
   if Nome.isalpha():
      break
   else:
     print('Nesse campo so pode usar letras')
print('______________________________________________________')
while True:
   try:
      N1 = float(input("N1:"))
      if N1 >10:
       print('Numero deve ser igual ou menor do que 10')
      else:
         break
   except ValueError:
      print('Nesse campo so pode usar numeros')
print('________________________________________________________')
while True:
   try:
      N2 = float(input("N2:"))
      if N2 >10:
       print('Numero deve ser igual ou menor do que 10')
      else:
         break
   except ValueError:
      print('Nesse campo so pode usar numeros')
   
print('____________________________________________________________')


Resultado = (N1 + N2) / 2

print()

if 9 < Resultado <=  10:
   print ('_____________')
   print (Nome)
   print (Resultado)
   print ('Aprovado')
   print ('A')

elif 7<= Resultado <=9:
   print ('_____________')
   print (Nome)
   print (Resultado)
   print ('Aprovado')
   print ('B')

elif 7 > Resultado >=6:
   print ('_____________')
   print (Nome)
   print (Resultado)
   print ('Recuperacao')
   print ('C')

elif 6 > Resultado:
   print ('_____________')
   print (Nome)
   print (Resultado)
   print ('Reprovado')
   print ('D')
   

