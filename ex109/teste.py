import moeda3

print(f'{" MOEDAS FORMATADAS ":-^40}')

preco = float(input('Digite o preço: R$ '))

print(f'''
{" RESULTADOS ": ^40}
• A metade de R$ {moeda.moeda(preco)} é {moeda.metade(preco, True)}
• O dobro de R$ {moeda.moeda(preco)} é {moeda.dobro(preco, True)}
• Aumentando 10% do preço, temos {moeda.aumentar(preco, True)}
• Diminuindo 10% do preço, temos {moeda.diminuir(preco, True)}
''')
