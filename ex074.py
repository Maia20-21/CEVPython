from random import randint

num = (randint(1,10), randint(1,10), randint(1,10), randint(1,10))

print(f'''Números sorteados: {num}
Maior: {sorted(num)[-1]}
Menor: {sorted(num)[0]}
''')