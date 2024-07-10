velocidade = float(input('Qual é a velocidade atual do carro? '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'''MULTADO! Você excedeu o limite permitido que é de 80km/h.
Pague sua multa de R$ {multa:.2f}!
''')
else:
    print('Velocidade dentro dos limites. Tenha um bom dia!')