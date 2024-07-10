print('SEQUÊNCIA DE FIBONACCI\n')

termos_solicitados = int(input('Quantos termos você quer mostrar da sequência? '))

n1 = 0
n2 = 1
termos = 0

while termos < termos_solicitados:
    print(f'{n1}', end= ' ➔ ')
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    termos += 1
print('FIM')


