print('''SOMA DE NÚMEROS INTEIROS
- digite vários números que deseja somar
- digite '999' caso queira exibir o resultado
''')

soma = num = int(input('Digite um número inteiro: '))

while num != 999:
    num = int(input('Digite um número inteiro: '))
    soma += num
print(f'A soma dos números inteiros é igual a {soma - 999}')