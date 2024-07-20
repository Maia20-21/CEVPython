print(f'{"VALIDANDO A ENTRADA DE DADOS":-^40}')

def leiaInt(msg):
    while True:
        num = input(msg)
        if num.isdigit():
            return int(num)
        else:
            print()
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
            print()

n = leiaInt('Digite um valor: ')
print(f'Você acabou de digitar o número {n}.')
