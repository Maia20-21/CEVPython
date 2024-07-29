from utilidadesCeV import moeda, dado

print(f'{" MOEDAS FORMATADAS ":-^40}')
preco = dado.leiaDinheiro('Digite o preço: R$ ')

moeda.resumo(preco)