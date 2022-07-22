#Escreva um programa que identifique se existe ou não a palavra Santo no início do
#nome da sua cidade.

cidade = str(input('Digite o nome da sua cidade: '))
print('{} para  Santo no início do nome da cidade.' .format('Santo' in cidade.split()[0]))