import random
from typing import List, Any

n1 = str(input('Digite o nome do primeiro aluno: '))
n2 = str(input('Digite o nome do segundo aluno:'))
n3 = str(input('Digite o nome do terceiro aluno: '))
n4 = str(input('Digite o nome do quarto aluno: '))
l = [n1, n2, n3, n4]
escolhido = random.choice(l)
print('O aluno sorteado é {}.' .format(escolhido))
