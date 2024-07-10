distancia = float(input('Qual é a distância da sua viagem? '))

if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45

print(f'''Você está prestes a começar uma viagem de {distancia} Km
E o preço da passagem é de R$ {preco:.2f}
''')