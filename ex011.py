l = float(input('Digite a largura (m) da parede: '))
h = float(input('Digite a altura (m) da parede: '))
a = l * h
t = a // 2
print('A área da parede é de {:.2f} metros quadrados e serão necessários {} litros de tinta' .format(a, t))
