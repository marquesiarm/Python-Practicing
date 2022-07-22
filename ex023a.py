#Escreva um programa que retorne os digitos separadamente de unidade, dezena,
#centena e milhar de um número de inteiro de quatro dígitos.
num = str(input('Digite um número inteiro positivo de quatro dígitos: '))
#print('unidade: {}' .format(num[len(num) - 1]))
#print('dezena: {}' .format(num[len(num) - 2]))
#print('centena: {}' .format(num[len(num) - 3]))
#print('milhar: {}' .format(num[0]))

print('unidade: {};' .format(num[3]))
print('dezena: {};' .format(num[2]))
print('centena: {};' .format(num[1]))
print('milhar: {};' .format(num[0]))