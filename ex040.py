#Crie um programa que leia duas notas de um aluno e calcule a sua média,
#mostrando uma mensagem no final, de acordo com o reusltado: reprovado para
#média menor do que 5; reuperação entre 5 e 6.9; aprovado para média 7 ou superior#

from numpy import mean
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = mean([n1, n2])
if m < 5:
    print('REPROVADO! Sua média foi {:.1f}.' .format(m))
elif 5 <= m <= 6.9:
    print('RECUPERAÇÃO! Sua média foi {:.1f}.' .format(m))
else:
    print('APROVADO! Sua média foi {:.1f}.' .format(m))
