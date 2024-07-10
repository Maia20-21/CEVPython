preco = float(input('Preço das compras: R$'))

print('''
FORMAS DE PAGAMENTO
[1] à vista dinheiro / cheque
[2] à vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão
''')

opcao = int(input('Qual é a sua opção: '))
print('')

if opcao == 1:
    preco_final = preco - preco * 0.1
    print(f'''10% de desconto
Preço final: R${preco_final}
''')

elif opcao == 2:
    preco_final = preco - preco * 0.05
    print(f'''5% de desconto
Preço final: R${preco_final}
''')

elif opcao == 3:
    print(f'''valor formal
Preço final: R${preco}
''')

elif opcao == 4:
    preco_final = preco + preco * 0.2
    print(f'''juros de 20%
Preço final: R${preco_final}
''')

else:
    print('Opção inválida. Tente novamente!')