palavras = ('estagio', 'emprego', 'mercado', 'trabalho', 'salario', 'programar', 'futuro', 'empresa')

print(f'{"VOGAIS NAS PALAVRA":^40}')
for palavra in palavras:
    print(f'\n{palavra}: ', end = '')
    for letra in palavra:
        if letra in 'aeiou':
            print(f'{letra}', end = ' ')