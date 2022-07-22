#Desenvolva uma lógica que leia o peso e a altura de um pessoa,
#calcule o seu IMC e mostre a sua condição como: abaixo do pesso para índice menor que 18.5;
#peso ideal para índice entre 18.5 e 25; sobrepeso para índice entre 25 e 30;
#obesidade entre 30 e 40; obesidade mórbida para índice acima de 40.#
alt = float(input('Digite a sua altura (m): '))
massa = float(input('Digite a sua massa (kg): '))
imc = massa / (alt ** 2)
if imc < 18.5:
    print('O seu IMC é {:.1f}. Você está abaixo do pesso ideal.' .format(imc))
elif 18.5 < imc < 25:
    print('O seu IMC é {:.1f}. Você está com peso ideal.' .format(imc))
elif 25 <= imc <= 30:
    print('O seu IMC é {:.1f}. Você está com sobrepeso.' .format(imc))
elif 30 < imc <= 40:
    print('O seu IMC é {:.1f}. Você está obeso.' .format(imc))
elif imc > 40:
    print('O seu IMC é {:.1f}. Você está com obsidade mórbida.' .format(imc))

#incluindo um comentário de texto para testar o git#
