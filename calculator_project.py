import os
import re

#Fuctions
def clear():
    if os.name == 'nt':
      os.system('cls')
    elif os.name == 'poxis':
      os.system('clear')

conta='0';
conta_inicial=[]
conta_list=''
padrao = r'(\d+|[-+*/])' #expressão regular todos os inteiros e operadores escolhidos


conta=input("introduza um conta de 2 ou mais digitos com 1 ou varias operações aritmeticas\n");
conta_inicial=conta
conta_list = re.findall(padrao, conta) #aplicar a expressao regular



while len(conta_list)>1:  

  for indice, digito in enumerate(conta_list):
    if digito == '*': 
        conta_list.pop(indice)
        conta_list.insert( indice-1, int(conta_list.pop(indice-1)) * int(conta_list.pop(indice-1)) )

    elif digito == '/': 
       conta_list.pop(indice)
       conta_list.insert( indice-1, int(conta_list.pop(indice-1)) / int(conta_list.pop(indice-1)) )

  for indice, digito in enumerate(conta_list):
      if digito == '+': 
        conta_list.pop(indice)
        conta_list.insert( indice-1, (int(conta_list.pop(indice-1) ) + int(conta_list.pop(indice-1) ) ) )

      elif digito == '-': 
        conta_list.pop(indice)
        conta_list.insert( indice-1, int(conta_list.pop(indice-1)) - int(conta_list.pop(indice-1)) )

print("Sua conta inicial é:",conta_inicial)
print("Resultado da conta é de:",conta_list[0])

