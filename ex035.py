r1 = float(input('Digite o primeiro comprimento (cm) de reta r1: '))
r2 = float(input('Digite o segundo comprimento (cm) de reta r2: '))
r3= float(input('Digite o terceiro comprimento (cm) de reta r3: '))
#A soma dos comprimentos de quaisquer dois seguimentos de um triângulo sempre
# deve ser maior do que o comprimento do seguinte restante.#
if r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2:
    print('É possível construir um triângulo a partir dos comprimentos de retas r1, r2 e r3.')
else:
    print('Não é possível construir um triângulo a partir dos comprimentos de retas r1, r2 e r3.')
