print(f'{' JOGADOR DE FUTEBOL ':-^50}')

jogos = {}

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

print(f'{' RESULTADO ':-^50}')
print(jogos)
print('-' * 50)

for k, v in jogos.items():
    print(f'O campo {k} tem valor {v}')
print('-' * 50)

print(f'O jogador {jogos['nome']} jogou {partidas} partidas')
for i in range(partidas):
    print(f'• na {i + 1}º partida, fez {jogos['gols'][i]} gols')