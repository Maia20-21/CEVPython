print(f'{' CADASTRO ':-^40}')

aluno = {}
aluno['nome'] = input('Nome do aluno: ')
aluno['média'] = float(input('Média: '))
print()

if aluno['média'] < 5:
    aluno['situação'] = 'REPROVADO'
elif aluno['média'] < 7:
    aluno['situação'] = 'RECUPERAÇÃO'
else:
    aluno['situação'] = 'APROVADO'

print(f'{' SITUAÇÃO ESCOLAR DO ALUNO ':-^40}')
print(f'''Nome: {aluno['nome']}
Média: {aluno['média']}
Situação: {aluno['situação']}
''')

