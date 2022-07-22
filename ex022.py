#Escreva um programa que solicite o nome completo de uma pessoa e retorne a forma
#escrita desse nome em letras maiúlculas e em letra minúsculas;
#apresente a quantidade total de letras no nome;
# e indique também a quantidade de letras no primeiro nome.
nome = str(input('Digite o seu nome completo: '))
print('O seu nome completo em letras maiúsculas é: {}.' .format(nome.strip().upper()))
print('O seu nome completo em letras minúsculas é: {}.' .format(nome.strip().lower()))
print('O seu nome completo possui {} letras.' .format(len(''.join(nome.strip().split()))))
print('O seu primeiro nome possui {} letras.' .format(len(''.join(nome.strip().split()[0]))))