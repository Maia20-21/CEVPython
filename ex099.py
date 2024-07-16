print(f'{' MAIOR VALOR INFORMADO ':-^60}')

def maior(* valores):
    print('Valores: ', end='')
    for valor in valores:
        print(valor, end=' ')
    print()
    print(f'Foram analisados {len(valores)} valores e o maior foi o número {max(valores)}')

maior(4, 6, 9, 2, 10)