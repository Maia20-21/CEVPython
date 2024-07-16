from datetime import datetime

print(f'{' CADASTRO DE TRABALHADOR ':-^40}')

dados = {}

nome = input('Nome: ')
dados['nome'] = nome

nasc = int(input('Ano de nascimento: '))
idade = datetime.now().year - nasc
dados['idade'] = idade

ctps = int(input('Carteira de Trabalho [0 - não tem]: '))
dados['ctps'] = ctps
if ctps != 0:
    ano_contratacao = int(input('Ano de contratação: '))
    dados['ano de contratação'] = ano_contratacao

    salario = float(input('Salário: '))
    dados['salário'] = salario

    aposentadoria = 65 - idade
    dados['aposentadoria'] = aposentadoria
print()

print(f'{' EXIBINDO OS RESULTADOS ':-^40}')

for chave, valor in dados.items():
    print(f'{chave} tem o valor de {valor}')

