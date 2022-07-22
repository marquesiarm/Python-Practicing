vel = float(input('Digite a velocidade (km/h) do carro: '))
if vel > 80:
    print('Você foi multado! A multa vai custar R${:.2f}' .format((vel - 80) * 7))
    print('Fim do programa')
else:
    print('Fim do programa')
