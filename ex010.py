""" Crie um programa que leia quanto dinheiro uma pessoa
tem na carteira e mostre quantos dolares ela pode comprar.

Considerando o câmbio = U$1,00 = R$3,27"""

print("Dollar baby\n")

wallet = float(input('Digite aqui quanto em dinheiro você quer cambiar: R$ '))
dol = (wallet/3.27)

print(f'Com R${wallet:.2f} você pode comprar U${dol:.2f}!')