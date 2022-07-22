from math import sqrt, hypot
op = float(input('Digite o comprimento do cateto oposto do triângulo retângulo: '))
ad = float(input('Digite o comprimento do cateto adjacente do triângulo retângulo: '))
#h = sqrt(op**2 + ad**2)
h = hypot(op, ad)
print('A hipotensa do triângulo retângulo com cateto oposto de {} e cateto adjacente de {} vale {:.2f}.' .format(op, ad, h))

