sb = float(input('Digite seu salário bruto: '))
i = float(input('Digite o desconto do INSS em porcentagem: '))

d = sb*(i/100)
sl = sb - d
print(f"Seu salário líquido é R${sl}")