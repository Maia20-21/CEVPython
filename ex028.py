from random import randint

print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-' * 55)

num = randint(0, 5)
x = int(input('Em que número eu pensei? '))

if x == num:
    print('Você GANHOU!')
else:
    print(f'Você PERDEU. Eu pensei no número {num}, e não no {x}')