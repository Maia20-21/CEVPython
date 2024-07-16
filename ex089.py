print(f'{' CADASTRO DE NOTAS ':-^30}')

lista = []
temp = []

while True:
    nome = input('\nNome: ')
    temp.append(nome)

    n1 = float(input('Nota 1: '))
    temp.append(n1)

    n2 = float(input('Nota 2: '))
    temp.append(n2)

    lista.append(temp[:])
    temp.clear()

    continuar = input('\nDeseja continuar [S/N]? ').upper().strip()
    if continuar != 'S':
        break

print(f'\n{' BOLETIM ':-^30}')

print(f'{'nº':<4} {'NOME':<10} {'MÉDIA':>8}')
for i, aluno in enumerate(lista):
    media = (aluno[1] + aluno[2]) / 2
    print(f'{i+1:<4} {aluno[0]:<10} {media:>8.2f}')