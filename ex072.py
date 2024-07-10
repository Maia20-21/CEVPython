tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    try:
        num = int(input('Digite um número entre 0 - 20: '))
        if 0 <= num <= 20:
            print(f'Você digitou o número {tupla[num]}')
            break
        else:
            print("Número fora do intervalo. Tente novamente.")
    except ValueError:
        print("Digite um NÚMERO INTEIRO. Tente novamente.")

# jeito prático
'''
lista = []

for i in range(0,21):
    lista.append(i)

while True:
    numero = int(input('Digite um número entre 0 - 20: '))
    while numero not in lista:
        print("Número fora do intervalo. Tente novamente.")
        numero = int(input('Digite um número entre 0 - 20: '))
    print(f'Você digitou o número {numero}, que está entre 0 e 20.')
    break
'''