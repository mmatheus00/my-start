"""
Faça um programa que leia a largura e a altura de uma parede
em metros, calcule a sua área e a quantidade de tinta necessária
para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²
"""

print('Tu pinta como eu pinto?\n')

alt = float(input('Digite a altura da parede em metros: '))
lar = float(input('Digite a largura da parede em metros: '))

area = (alt*lar)
tinta = ((alt*lar)/2)

print(f'A área da sua parede é de {area:.2f}m²\n'
      f'para pinta-lá vão ser necessários {tinta} litros de tinta!\n'
      f'Caso necessite de duas demãos, serão necessários {(tinta*2)} litros de tinta!')