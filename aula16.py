# if / elif      / else
# se / se não se / se não
usuario = 'Matheus Lopes'
entrada = input('Você quer "entrar" ou "sair"? ')

if entrada == 'entrar':
    print('Você entrou no sistema')
    print(f'Seja bem vindo {usuario}!')
elif entrada == 'sair':
    print('Você saiu do sistema')
    print(f'Até mais {usuario}!')
else:
    print('Você não digitou nem entrar e nem sair.')
    print('Por favor, digite "entrar" ou "sair".')


