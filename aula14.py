a = 'A'
b = 'B'
c = 1.1
#string = 'a={0} b={1} c={2:.2f}' # Tanto faz com ou sem a variável string, pode ser feito tudo na linha 5
string = 'a={nome1} b={nome2} c={nome3:.2f}' # Pode ser chamado por índices -> 0, 1, 2... ou por parâmetros nomeados -> nome3=c
formato = string.format(nome1=a, nome2=b, nome3=c) #format(a, b, c = argumento) -> format(nome=a) parâmetro nomeado

print(formato)