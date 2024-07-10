casa = int(input('Valor da casa: '))
salario = int(input('Salário do comprador: '))
tempo = int(input('Anos de financiamento: '))

prestacao = casa / (tempo * 12)

print(f'Para pagar uma casa de R${casa:.2f} em {tempo} anos, a prestação será de R${prestacao:.2f}')
if prestacao > 0.3 * salario:
    print('Empréstimo NEGADO')
else:
    print('Empréstimo APROVADO')