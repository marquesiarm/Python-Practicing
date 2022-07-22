from math import sin, cos, tan, pi, radians
theta = float(input('Digite o valor do ângulo em graus: '))
#print('Os valores das funções cosseno, seno e tangente para o ângulo {} são, respectivamente, {:.2f}, {:.2f} e {:.2f}.' .format(theta, cos(pi * theta / 180), sin(pi * theta / 180), tan(pi * theta / 180)))
seno = sin(radians(theta))
cosseno = cos(radians(theta))
tangente = tan(radians(theta))
print('As funções trigonométricas para o ângulo {}º possuem valores: sen = {:.2f}; cos = {:.2f} e tg = {:.2f}.' .format(theta, seno, cosseno, tangente))