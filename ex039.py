from datetime import date

atual = date.today().year
nascimento = int(input('Ano do seu nascimento: '))
idade = atual - nascimento

print(f'Quem nasceu em {nascimento} tem {idade} anos em {atual}')

if idade < 18:
    print(f'''Ainda falta {18 - idade} ano(s) para o alistamento.
Seu alistamento será em {atual + (18 - idade)}.
''')

elif idade > 18:
    print(f'''Você já deveria ter se alistado há {idade - 18} ano(s)
Seu alistamento foi em {atual - (idade - 18)}.''')

else:
    print('Você tem que se alistar IMEDIATAMENTE')