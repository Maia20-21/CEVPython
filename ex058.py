from random import randint

print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-' * 55)

num = randint(0, 10)
x = int(input('Em que número eu pensei? '))
tentativas = 0

while x != num:
    if x < num:
        print('Mais...Tente novamente')
        x = int(input('Em que número eu pensei? '))
        tentativas += 1
    else:
        print('Menos...Tente novamente')
        x = int(input('Em que número eu pensei? '))
        tentativas += 1

print(f'''
Você GANHOU!
Foram necessárias apenas {tentativas} tentativas
''')
