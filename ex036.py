valor_casa = float(input('Qual é o valor da casa? '))
salario = float(input('Qual é o valor do seu salário? R$ '))
tempo = float(input('Em quantos anos deseja quitar o empréstimo: '))
prestação = valor_casa / (tempo * 12)
if prestação < 0.30 * salario:
    print('Parabéns! Seu empréstimo foi aprovado.')
    print('O valor da sua prestação mensal será de R$ {:.2f}.' .format(prestação))
else:
    print('Infelizmente o seu empréstimo não foi aprovado.')