ano = input('Que ano você gostaria de analisar? ')

num = ano[-2] + ano[-1]

if int(num) % 4 == 0:
    print(f'O ano {ano} é BISSEXTO!')
else:
    print(f'O ano {ano} não é bissexto!')
