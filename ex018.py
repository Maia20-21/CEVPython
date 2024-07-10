import math                                                      # from math import radian, sin...
x = float(input('Digite o valor de um ângulo: '))
sen = math.sin(math.radians(x))                                  # sen = sin(radians(x))
cos = math.cos(math.radians(x))
tang = math.tan(math.radians(x))

print(f'Seno = {sen:.2f} \nCosseno = {cos:.2f} \nTangente = {tang:.2f}')