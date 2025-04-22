# Escreva um programa que leia um valor em metros e o exiba em centímetros e milímetros.

print('Conversor de medidas')

met = float(input('Digite o valor em metros que precisa ser convertido: '))

print(f'Convertendo {met} metros obtemos...\n'
      f'{met*100:.2f} centímetros\n'
      f'e {met*1000:.2f} milímetros')