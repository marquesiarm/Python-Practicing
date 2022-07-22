#Refaça o ex035 acrescentando o recurso de mostrar que tipo de triângulo
#será formado. Equilátero, isóceles ou escaleno?#

l1 = float(input('Digite o comprimento (m) do primeiro segmento de reta: '))
l2 = float(input('Digite o comprimento (m) do segundo segmento de reta: '))
l3 = float(input('Digite o comprimento (m)  do terceiro segmento de reta: '))
if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    #print('É possivel formar um triângulo com os três segmentos de retas')
    if l1 == l2 == l3:
        print('É possível formar um triângulo EQUILÁTERO com os segmentos de reta.')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('É possível formar um triângulo ISÓCELES com os segmentos de reta.')
    else:
        print('É possível formar um triângulo ESCALENO com os segmentos de reta.')
else:
    print('Não é possível formar um triângulo com os segmentos de retas.')
