nome = input('Digite seu nome completo: ')
nome = nome.strip().split()

print(f'''
Primeiro nome: {nome[0]}
Último nome: {nome[-1]}
''')