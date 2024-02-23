primeiro_valor = input('Primeiro valor: ')
segundo_valor = input('Segundo valor: ')

if primeiro_valor >= segundo_valor:
        #print('primeiro valor é maior que o segundo valor')
        print(f'{primeiro_valor=} é maior ou igual ao {segundo_valor=}')
elif segundo_valor >= primeiro_valor:
        #print('segundo valor é maior que o primeiro valor')
        print(f'{segundo_valor=} é maior ou igual ao {primeiro_valor=}')

else:
        print('Sem valores')