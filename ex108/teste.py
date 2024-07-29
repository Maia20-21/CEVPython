import moeda2

print(f'{" MOEDAS FORMATAS ":-^40}')

preco = float(input('Digite o preço: R$ '))

print(f'''
{" RESULTADOS ": ^40}
• A metade de R$ {moeda.moeda(preco)} é {moeda.moeda(moeda.metade(preco))}
• O dobro de R$ {moeda.moeda(preco)} é {moeda.moeda(moeda.dobro(preco))}
• Aumentando 10% do preço, temos {moeda.moeda(moeda.aumentar(preco))}
• Diminuindo 10% do preço, temos {moeda.moeda(moeda.diminuir(preco))}
''')