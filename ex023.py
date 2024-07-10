x = int(input('Digite um número de 0 - 9999: '))
u = x // 1 % 10
d = x // 10 % 10
c = x // 100 % 10
m = x // 1000 % 10

print('Analisando o número...')

print(f'''unidade: {u}
dezena: {d}
centena: {c}
milhar: {m}''')