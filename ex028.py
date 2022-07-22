from random import randint
numpc = randint(0, 5)
num = int(input('Adivinhe e digite um número que o pc pensou entre 0 e 5: '))
if num == numpc:
    print('PARABÉNS! Você acertou')
else:
    print('Você errou! Tente novamente.')
