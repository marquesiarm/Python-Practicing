from random import randint
num = int(input('Adivinhe e digite um número entre 0 e 5 que o pc pensou: '))
print('PARABÉNS, você acertou!' if num == randint(0, 5) else 'Você errou, tente novamente.')
