# Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa. O programa vai perguntar o valor da casa, o salarioo do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30%  do salario ou então o emprestimo sera negado.
vlrCasa = float(input('Qual o valor da casa? '))
vlrSalario = float(input('Qual o valor do salario? '))
anos = int(input('Em quantos anos a casa sera paga? '))

vlrMensal = vlrCasa / (anos * 12)

if vlrMensal > (vlrSalario*0.30):
    print('O emprestimo foi negado!')
else:
    print('O emprestimo foi aprovado e o valor mensal a ser pago é {:.2f}'.format(vlrMensal))