"""
Formatação básica de strings
s - string
d e i - int
f - float
.<número de dígitos>f
x e X - Hexadecimal (ABCDEF0123456789)
(Caractere) (><^) (quantidade)
> - esquerda
< - direita
^ - centro
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a
"""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel: ^10}')
print(f'{1000.654651521614:,.2f}')