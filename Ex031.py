dist = float(input('Digite a distância (km) do percurso: '))
if dist <= 200:
    print('O preço da passagem é R${:.2f}.' .format(0.50 * dist))
    print('Fim')
else:
    print('O preço da passagem é R${:.2f}.' .format(0.45 * dist))
    print('Fim')
