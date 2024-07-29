import moeda1

print(f'{' MOEDAS SEM FORMATAÇÃO ':-^40}')

preco = int(input('Digite o preço: R$ '))

print(f'''
{' RESULTADOS ': ^40}
• A metade de R$ {preco:.2f} é R$ {moeda.metade(preco):.2f}
• O dobro de R$ {preco:.2f} é R$ {moeda.dobro(preco):.2f}
• Aumentando 10% do preço, temos R$ {moeda.aumentar(preco):.2f}
• Diminuindo 10% do preço, temos R$ {moeda.diminiuir(preco):.2f}''')