cores = {
    'limpa':'\033[m',
    'vermelho':'\033[31m'
}

def leiaDinheiro(msg):
    while True:
        msg = str(input('Digite o preço: R$ ')).strip().replace(',', '.')
        if msg == '' or msg in " ":
            print(f'\n{cores['vermelho']}Entrada inválida! Tente novamente.{cores['limpa']}\n')
        elif msg.isalpha() or msg.isalnum():
            print(f'\n{cores['vermelho']}{msg} é um preço inválido! Tente novamente.{cores['limpa']}\n')
        else:
            return float(msg)