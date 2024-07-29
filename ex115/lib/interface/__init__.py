def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except:
            print('\n\033[31mERRO! Por favor, digite um número inteiro válido.\033[m\n')
        else:
            return n

def cabeçalho(txt, tamanho = 40):
    print('-' * tamanho)
    print(f'{txt: ^{tamanho}}')
    print('-' * tamanho)

def linha(tamanho = 40):
    print('-' * tamanho)


def menu(lista):
    cabeçalho(' MENU PRINCIPAL ')
    c = 1
    for i in lista:
        print(f'{c} - {i}')
        c += 1
    linha()
    opcao = leiaInt('Sua opção: ')
    return opcao