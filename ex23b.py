#Escreva um programa que solicite o nome completo de uma pessoa e retorne a forma
#escrita desse nome em letras maiúlculas e em letra minúsculas;
#apresente a quantidade total de letras no nome;
# e indique também a quantidade de letras no primeiro nome.

num = int(input('Digite um número interiro entre 0 e 9999: '))

#print('unidade: {}' .format(num % 10))
#print('dezena: {}' .format((num - (((num // 1000)*1000) + ((num - (num // 1000)*1000) // 100) * 100)) // 10))
#print('centena: {}' .format((num - (num // 1000)*1000) // 100))
#print('milhar: {}' .format(num // 1000))

#outra maneira:

print('unidade: {};' .format(num // 1 % 10))
print('dezena: {};' .format(num // 10 % 10))
print('centena: {};' .format(num // 100 % 10))
print('milhar: {};' .format(num // 1000 % 10))
