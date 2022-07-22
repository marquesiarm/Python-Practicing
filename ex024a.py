#Escreva um programa que identifique se o nome da sua cidade inicia-se com "Santo".

cid = str(input('Digite o nome da sua cidade: ')).strip()
print('É {} que o nome da sua cidade inicia-se com "Santo".' .format(cid[:5].upper() == 'SANTO'))
