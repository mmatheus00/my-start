# Programa 004 - Tipo, quantidade e se os caracteres são minusculos
a1 = input('Digite algo: ')

print('qual o tipo dos dados? ', type(a1))
print('sua resposta tem', len(a1), 'caracteres!')
print('são todos lowercase? ', a1.islower())
print('é um número? ', a1.isnumeric())
