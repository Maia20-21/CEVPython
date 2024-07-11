print('DIVIDINDO VALORES EM PAR OU ÍMPAR')

lista = []
par = []
impar = []

while True:
    x = int(input('\nDigite um valor: '))
    lista.append(x)
    if x % 2 == 0:
        par.append(x)
    else:
        impar.append(x)

    resposta = input('Deseja continuar [S / N]: ').upper()
    if resposta != 'S':
        break
print(f'''
Lista completa: {lista}
Pares: {par}
Ímpares: {impar}
''')