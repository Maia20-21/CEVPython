print('VALIDANDO EXPRESSÕES MATEMÁTICAS\n')
# uso correto - falando de quantidade - dos parênteses


p_aberto = []
p_fechado = []

expressao = input('Digite uma expressão matemática simples: ')
for caractere in expressao:
    if caractere == '(':
        p_aberto.append('(')
    elif caractere == ')':
        p_fechado.append(')')
if len(p_aberto) == len(p_fechado):
    print('Sua expressão está CORRETA')
else:
    print('Sua expressão está INCORRETA')


