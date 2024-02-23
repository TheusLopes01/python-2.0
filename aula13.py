nome = 'Matheus Lopes'
altura = 1.70
peso = 75
imc = peso / (altura * altura)

# f-strings
linha_1 = f'{nome} tem {altura:.2f} de altura' # converter para dinheiro com vírgula -> :,.2f
linha_2 = f'Pesa {peso} quilos e seu IMC é: {imc:.2f}'
print(linha_1)
print(linha_2)
