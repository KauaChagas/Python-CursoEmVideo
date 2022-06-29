from math import radians, sin, cos, tan

ang = float(input('Digite um angulo: '))
angulo = radians(ang)

print(f'O seno de {int(ang)}° é {sin(angulo):.2f}')
print(f'O cosseno de {int(ang)}° é {cos(angulo):.2f}')
print(f'A tangente de {int(ang)}° é {tan(angulo):.2f}')

