from lib.interface import *

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')   # abrir para Leitura e Texto
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')      # Escrever arquivo de Texto, +: se não existir, criar
        a.close()
    except:
        print('\n\033[31mHouve um erro na criação do arquivo!\033[m\n')
    else:
        print(f'\n\033[32mArquivo {nome} criado com sucesso!\033[m\n')

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabeçalho(' PESSOAS CADASTRADAS ')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()

def cadastrar(arquivo, nome = 'desconhecido', idade = 0):
    try:
        a = open(arquivo, 'at')        # a: append
    except:
        print('Erro ao abrir o arquivo!')
    else:
        try:
            a.write(f'{nome}; {idade}\n')
        except:
            print('Erro ao escrever os dados!')
        else:
            print(f'\033[32mNovo registro para {nome} foi adicionado.\033[m\n')
            a.close()

