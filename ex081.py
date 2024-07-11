print('EXTRAINDO DADOS DE UMA LISTA')

lista = []

while True:
    x = int(input('\nDigite um valor: '))
    lista.append(x)

    resposta = input('Deseja continuar [S/N]: ').upper()
    if resposta not in 'S':
        break

lista.sort(reverse = True)

print(f'''
Quantidade de números digitados: {len(lista)}
Lista de valores em forma decrescente: {lista}''')

if 5 in lista:
    print('O valor 5 está na lista')
else:
    print('O valor 5 não está na lista')