# Sobre operador 'not'
senha = input('Senha: ')

if not senha:
    print("Voce nao colocou nada")
elif senha == '1':
    print('Voce entrou')
else:
    print('Voce saiu')