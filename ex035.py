a = float(input('1º segmento: '))
b = float(input('2º segmento: '))
c = float(input('3º segmento: '))

if a+b>c and a+c>b and b+c>a:
    print('Os segmentos informados PODEM formar um triângulo')
else:
    print('Os segmentos informados NÃO PODEM formar um triângulo')