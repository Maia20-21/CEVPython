sexo = input('Informe o seu sexo [F/M]: ').upper().strip()

while sexo not in 'MmFm':
    sexo = input('Dados inválido. Informe o seu sexo [F/M]: ').upper().strip()

print(f'Sexo {sexo} registrado')
