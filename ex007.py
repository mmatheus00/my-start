# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média

print('Médias escolares')

m = str(input('Digite aqui o nome da máteria: '))
n1 = float(input('Digite aqui sua primeira nota dessa matéria: '))
n2 = float(input('Digite aqui sua segunda nota dessa matéria: '))

print(f'Suas notas em {m} foram {n1} e {n2}?\n'
      f'Então, sua média na matéria é {(n1+n2)/2}! ')