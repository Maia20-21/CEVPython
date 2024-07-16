print(f'{' JOGADORES DE FUTEBOL ':-^50}')
#cadastro de vários jogadores

jogadores = []
jogos = {}

while True:
    nome = input('Nome do jogador: ')
    jogos['nome'] = nome

    partidas = int(input('Número de partidas: '))
    print()
    jogos['gols'] = []
    jogos['total'] = 0

    for i in range(partidas):
        gols = int(input(f'Quantidade de gols na {i+1}º partida: '))
        jogos['gols'].append(gols)
        jogos['total'] += gols
    print()

    jogadores.append(jogos.copy())
    jogos.clear()

    continuar = input('Deseja continuar [S/N]? ').upper()
    if continuar != 'S':
        break
    print()
print()

print(f'{' RESULTADOS ':-^50}')
print(f'{'Nº': <5}{'NOME': <15}{'GOLS': <20}{'TOTAL': <10}')
print('-'*50)

for i, jogador in enumerate(jogadores):
    print(f'{i + 1: <5}', end='')
    print(f'{jogador['nome']: <15}', end='')
    print(f'{str(jogador["gols"]): <20}', end='')
    print(f'{jogador["total"]: <10}')
