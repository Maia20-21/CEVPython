from random import randint

print(f'{' JOGO DOS DADOS ':-^30}')

dado = {}

jogadores = int(input('Número de jogadores: '))
print()

for i in range(jogadores):
    num = randint(1, 6)
    dado[f'jogador {i+1}'] = num

dado_ordenado = sorted(dado.items(), key=lambda x: x[1], reverse=True)

print(f'{' RANKING ':-^30}')
for i, (jogador, valor) in enumerate(dado_ordenado):
    print(f'{i+1}º lugar: {jogador} com {valor}')

