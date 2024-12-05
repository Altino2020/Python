ano = int(input('Coloca um ano aqui: '))
if(ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print('Bissesto')
else:
    print('Normal')