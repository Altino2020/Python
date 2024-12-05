# A aula e sobre os operadores logicos and (e) or (ou) not (nao)
entrada = input('[E]entrar [S]air ')
senha_digitada = input('Senha: ')
senha_permitida = '1984'
if entrada == 'E' and senha_digitada == senha_permitida:
    print('Bem Vindo')
else:
    print('Voce nao quis entrar ou sena incorreta')