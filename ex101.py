print(f'{' IDADE PARA VOTAR ':-^40}')

from datetime import date

def voto(ano_nascimento):
    data_atual = date.today().year
    idade = data_atual - ano_nascimento

    if idade < 16:
        print(f'Com {idade} anos: NÃO VOTA')
    elif idade < 18:
        print(f'Com {idade} anos: VOTO OPCIONAL')
    else:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO')

nascimento = int(input('Em que ano você nasceu? '))
voto(nascimento)