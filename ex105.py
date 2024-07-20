print(f'{' NOTAS ESCOLARES ':-^40}')

def notas(*valores, situacao = False):
    notas_dicionario = {}
    notas_lista = []

    for i in valores:
        notas_lista.append(i)
    notas_dicionario['total'] = len(notas_lista)

    notas_lista.sort()
    notas_dicionario['maior'] = notas_lista[-1]
    notas_dicionario['menor'] = notas_lista[0]

    notas_dicionario['média'] = sum(notas_lista) / len(notas_lista)

    if situacao == True:
        if notas_dicionario['média'] < 5:
            notas_dicionario['situação'] = 'PÉSSIMA'
        elif notas_dicionario['média'] < 8:
            notas_dicionario['situação'] = 'BOA'
        else:
            notas_dicionario['situação'] = 'EXCELENTE'

    print(notas_dicionario)

notas(3, 5, 9, 8, situacao = True)
