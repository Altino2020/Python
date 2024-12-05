# Operadores 'in' e 'not in'

nome = input('Digite o seu nome: ')
encontrar = input('Digite o que pretende encontrar no nome: ')

if encontrar in nome:
    print(f'{encontrar} esta em {nome}')
else:
    print(f'{encontrar} nao esta em {nome}')