num = int(input('Digite um número inteiro: '))

base = int(input('''Escolha uma das bases para conversão:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL
Sua opção: 
'''))

if base == 1:
    print(f'{num} convertido para BINÁRIO é igual a {bin(num)[2:]}')
elif base == 2:
    print(f'{num} convertido para OCTAL é igual a {oct(num)[2:]}')
elif base == 3:
    print(f'{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}')
else:
    prinr('Opção inválida. Tente novamente!')