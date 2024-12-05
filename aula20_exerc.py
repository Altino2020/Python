primeiro_valor = input('Coloca um primeiro valor numerico aqui ')
segundo_valor = input('Coloca um segundo valor numerico aqui ')

if primeiro_valor > segundo_valor:
    print(f"{primeiro_valor=} e maoir que o {segundo_valor=}")
elif primeiro_valor < segundo_valor:
    print(f"{segundo_valor=} e maoir que o {primeiro_valor=}")
else:
    print(f"{primeiro_valor=} e igual que o {segundo_valor=}")