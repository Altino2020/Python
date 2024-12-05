# A aula e sobre os operadores logicos 'and' (e), 'or' (ou) e 'not' (nao): depois de ter abordado o operador 'and' (aula 21) agora vai debrucar sobre o operador 'or'
entrada = input('[E]entrar [S]air ')
senha_digitada = input('Senha: ')
senha_permitida = '1984'
if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Bem Vindo')
else:
    print('Voce nao quis entrar ou senha incorreta')