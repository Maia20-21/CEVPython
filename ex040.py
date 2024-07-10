nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))

media = (nota1 + nota2) / 2

if media < 5:
    print(f'Sua média foi {media}. Você está REPROVADO!')
elif 7 > media >= 5:
    print(f'Sua média foi {media}. Você está de RECUPERAÇÃO!')
else:
    print(f'Sua média foi {media}. Você está APROVADO!')