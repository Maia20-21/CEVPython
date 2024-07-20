print(f'{' FICHA DO JOGADOR ':-^40}')

def ficha(nome = '', gols = 0):
    nome = input('Nome do jogador: ')
    if nome.strip() == '':
        nome = '<desconhecido>'

    gols = int(input('Número de gols: '))

    print(f'\nO(a) jogador(a) {nome} fez {gols} gol(s)')

ficha()