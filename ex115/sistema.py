from lib.interface import *
from lib.arquivo import *
from time import sleep

arquivo = 'cursoemvideo.txt'

if not arquivoExiste(arquivo):
    criarArquivo(arquivo)

while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        lerArquivo(arquivo)
    elif resposta == 2:
        cabeçalho(' CADASTRAR NOVA PESSOA ')
        nome = input('Nome: ')
        idade = leiaInt('Idade: ')
        cadastrar(arquivo, nome, idade)
    elif resposta == 3:
        print('\nSaindo do sistema...')
        break
    else:
        print('\n\033[31mResposta inválida! Digite uma opção válida\033[m\n')
    sleep(1)
