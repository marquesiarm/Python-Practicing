#Faça um programa que leia o ano de nascimento de uma pessoa e o informe, de acordo co ma sua idade:
#se ele ainda vai se alista ao serviço militar; se é a hora de se alistar;
# se já passou do tempo do alistmaento.#
import datetime
ano = int(input('Digite o ano do seu nascimento: '))
if ano + 18 > datetime.date.today().year:
    print('Ainda não é tempo de fazer o seu alistamento.\nSeu alistamento deverá ser realizado no período de Janeiro a Junho de {}.' .format(ano + 18))
elif ano == datetime.date.today().year:
    print('É tempo de realizar o seu alistamento! Seu alistamento militar deve ser feito até Junho deste ano. ')
else:
    print('Já passou do tempo do seu alistmaento! O prazo final do seu alistmento encerrou em 30/06/{}.' .format(ano + 18))
