a = float(input('Digite o primeiro valor: '))
b = float(input('Digite o segundo valor: '))
c = float(input('Digite o terceiro valor: '))

# Verificando qual número é menor. #
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

# Verificando qual númeor é maior. #
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O MENOR número digitado é {}.' .format(menor))
print('O MAIOR número digitado é {}.' .format(maior))
