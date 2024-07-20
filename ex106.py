from time import sleep

cores = {'vermelho': '\033[31m',
         'verde': '\033[32m',
         'azul': '\033[34m',
         'limpa': '\033[m',
         'fundo branco': '\033[40;97m'}

print(f'{' INTERACTIVE HELPING SYSTEM - PyHELP ':=^60}')

def ajuda(comando):
    help(comando)

while True:
    comando = input('Função ou Biblioteca: ')
    print(f'Acessando o manual do comando {cores['vermelho']}{comando}{cores['limpa']}...\n')
    sleep(1)

    print(cores['fundo branco'])
    print(ajuda(comando))
    print(cores['limpa'])

    continuar = input('Deseja continuar [S/N]: ').upper().strip()
    print()
    if continuar != 'S':
        break
print(f'{cores['vermelho']}{'Fechando o programa...'}{cores['limpa']}')
