print(f'{' VALIDAÇÃO DE DADOS ':-^40}')

def leiaInt():
    while True:
        try:
            n = int(input('Digite um número inteiro: '))
        except:
            print('\n\033[31mERRO! Por favor, digite um número inteiro válido.\033[m\n')
        else:
            return n

def leiaFloat():
    while True:
        try:
            n = float(input('Digite um número real: '))
        except:
            print('\n\033[31mERRO! Por favor, digite um número real válido.\033[m\n')
        else:
            return n

n = leiaInt()
m = leiaFloat()

print(f'{' RESULTADOS ':-^40}')
print(f'''Valor inteiro: {n}
Valor real: {m}
''')

