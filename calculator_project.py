import os

#Fuctions
def clear():
    if os.name == 'nt':
      os.system('cls')
    elif os.name == 'poxis':
      os.system('clear')


#conta=input("introduza um conta de 2 ou mais digitos com 1 ou varias operações aritmeticas\n");
conta='2+5-8*4'
conta_list=list(conta);
nova_lista=[]

for indice, digito in enumerate(conta_list):
    if digito == '*' or digito == '/':
        nova_lista.append(conta_list[indice])
    print(f'indice {indice}, digito {digito}')

print(conta_list)
print(nova_lista)


# * / + -