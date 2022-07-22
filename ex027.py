#Faça um programa que leia o nome completo de uma pessoa e mostre separadamente o primeiro e o
#último nome.
nome = str(input('Digite o seu nome completo: '))
print('primeiro nome: {};' .format(nome.strip().split()[0]))
print('último nome: {}.' .format(nome.strip().split()[len(nome.strip().split()) -1]))
