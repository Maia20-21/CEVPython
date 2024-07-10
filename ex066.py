print('SOMA DE NÚMEROS INTEIROS')

lista = []

while True:
    num = int(input('Digite um número [parar: "999"]: '))
    if num == 999:
        break
    lista.append(num)
print(f'''
Números digitados: {len(lista)}
Soma: {sum(lista)}
''')
