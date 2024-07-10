peso = float(input('Digite seu peso (Kg): '))
altura = float(input('Digite sua altura (m): '))

imc = peso / altura ** 2

print(f'IMC: {imc:.2f}')

if imc > 40:
    print('Você está em OBESIDADE MÓRBIDA')
elif imc > 30:
    print('Você está em OBESIDADE')
elif imc > 25:
    print('Você está em SOBREPESO')
elif imc > 18.5:
    print('Você está no seu PESO IDEAL')
else:
    print('Você está ABAIXO DO PESO')