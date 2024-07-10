x = input('Digite algo: ')

print('O tipo primitivo desse valor é: ', type(x))
print('É um número? ', x.isnumeric())
print('É alfabético? ', x.isalpha())
print('É composto por números ou letras? ', x.isalnum())
print('É maiúscula? ', x.isupper())
print('É minúsculo? ', x.islower())
print('Está capitalizada? ', x.istitle())
print('Só tem espaços? ', x.isspace())

