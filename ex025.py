#Escreva um programa que verifique se existe Silva no nome de uma pessoa.

#nome = str(input('Digite o seu nome: '))
#print('{} para Silva no nome {}.' .format('Silva' in ''.join(nome.strip().split()), nome))

nome = str(input('Digite o seu nome: ')).strip()
print('{} para Silva no nome {}.' .format('silva' in nome.lower(), nome))
