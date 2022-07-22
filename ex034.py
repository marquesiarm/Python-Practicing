salario = float(input('Digite o valor do seu salário atual: R$ '))
if salario > 1250:
    print('Seu novo salário é de R${:.2f}, aumento de 10 %.' .format(salario * 1.1))
else:
    print('Seu novo salário é de R${:.2f}, aumento de 15 %.' .format(salario * 1.15))
