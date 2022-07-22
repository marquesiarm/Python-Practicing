#A confederação Nacioanl de natação precisa de um programa que leia o ano de nascimento
#de uma atleta e mostre a sua categoria de acordo com: até 9 anos - mirim; até 14 anos - infantil;
#até 19 anos - júnior; até 20 anos - sênior; acima master.#

from datetime import date
ano = int(input('Digite o ano do seu nascimento: '))
idade = date.today().year - ano
if idade <= 9:
    print('A sua categoria é MIRIM.')
elif 9 < idade <= 14:
    print('A sua categoria é INFANTIL.')
elif 14 < idade <= 19:
    print('A sua categoria é JUNIOR.')
elif 19 < idade <= 20:
    print('A sua categoria é SÊNIOR')
else:
    print('A sua categoria é MASTER.')
