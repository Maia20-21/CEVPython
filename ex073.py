print('TABELA DO CAMPEONATO BRASILEIRO DE FUTEBOL DE 2023\n')

times = ('Palmeiras', 'Grêmio', 'Atlético-MG', 'Flamengo', 'Botafogo', 'Bragantino', 'Fluminense', 'Athletico-PR', 'Internacional', 'Fortaleza', 'São Paulo', 'Cuiabá', 'Corinthians', 'Cruzeiro', 'Vasco', 'Bahia', 'Santos', 'Goiás', 'Coritiba', 'América-MG')

print(f'Os 5 primeiros times: {times[0:5]}\n')

print(f'Os 4 últimos colocados: {times[-1:-5: -1]}\n')

print(f'Em ordem alfabética: {sorted(times)}\n')

print(f'O Corinthians está na posição: {times.index('Corinthians')+1}')


