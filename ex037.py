num = int(input('Digite um número inteiro qualquer: '))
base = str(input('Escolha a base de conversão entre binário, octal ou hexadecimal: ')).lower().strip()

if base == 'binário':
    print('O número {} convertido para a base {} é {}.' .format(num, base, bin(num)))
elif base == 'octal':
    print('O número {} convertido para a base {} é {}.' .format(num, base, oct(num)))
elif base == 'hexadecimal':
    print('O número {} convertido para a base {} é {}.' .format(num, base, hex(num)))
else:
    print('Não foi possível realizar a conversão. Por favor, tente novamente.')