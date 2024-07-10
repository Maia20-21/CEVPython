salario = int(input('Qual é o salário do funcionário? '))

if salario > 1250:
    salario += 0.1 * salario
else:
    salario += 0.15 * salario

print(f'O novo salário será de R${salario:.2f}')
