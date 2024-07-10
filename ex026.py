frase = input('Escreva uma frase: ')
frase = frase.strip().upper()

print(f'''
Quantas vezes aparece a letra 'A': {frase.count('A')}
1º ocorrência: {frase.find('A')+1}
Última ocorrência: {frase.rfind('A')+1} 
''')