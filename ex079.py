lista = []

while True:
    x = int(input('\nDigite um valor: '))
    if x not in lista:
        lista.append(x)
    else:
        print('Valor duplicado. O valor digitado não será adicionado à lista!')

    resposta = input('\nDeseja continuar [S/N]: ').upper().strip()
    if resposta not in 'S':
        break

lista_ordenada = sorted(lista)
print(f'\nNúmeros em ordem crescente: {lista_ordenada}')