print(f'{' TÍTULO PERSONALIZADO ':-^30}')
def escreva(txt):
    print('-' * 30)
    print(f'{txt: ^30}')
    print('-' * 30)

txt = input('Escreva o título que desejar: ')
escreva(txt)