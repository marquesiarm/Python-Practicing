import random
n1 = str(input('Nome do 1º aluno: '))
n2 = str(input('Nome de 2º aluno: '))
n3 =str(input('Nome do 3º aluno: '))
n4 = str(input('Nome do 4º aluno: '))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A ordem de apresentações será:')
print(lista)