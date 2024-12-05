# Funcao imput: funciona de forma semelhante ao scanf da linguagem C
numero = int (input('Digite um numero: '))
resto = numero % 2
if resto == 0: 
    print("Par")
else: 
    print("Impar")

print(f"O numero que colocou e {numero}")