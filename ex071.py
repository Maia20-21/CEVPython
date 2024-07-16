print(f'{" CAIXA ELETRÔNICO ":-^55}')
print('• Possuímos cédulas de R$ 100, R$50, R$20, R$10 e R$1\n')

valor = int(input('Qual valor você deseja sacar? R$'))
total = valor
cedulas = [100, 50, 20, 10, 1]
resultado = {}

for cedula in cedulas:
    quantidade = total // cedula
    if quantidade > 0:
        resultado[cedula] = quantidade
        total -= quantidade * cedula

print(f'\n{" EXTRATO ":-^30}')
for cedula, quantidade in resultado.items():
    print(f'Cédulas de R${cedula}: {quantidade}')

print(f'{" FIM DA TRANSAÇÃO ":-^30}')