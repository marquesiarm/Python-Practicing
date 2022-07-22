# Escreva um programa que identifique a quantiadde de repetições e posição da primeira e última
# letra "a" em uma frase.

frase = str(input('Digite uma frase: ')).strip().lower()
print('A letra "a" aparece {} vezes na frase.' .format(frase.count('a')))
print('A primeira ocorrência da letra "a" na frase é na poisção com índice {}.' .format(frase.find('a')))
print('A última ocorrência da letra "a" é na posição com índice {}.' .format(frase.rfind('a')))

