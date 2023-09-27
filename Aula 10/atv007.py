# Escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento. Para salarios superiores a R$ 1.250,00, calcule um aumento de 10% e salarios inferiores ou iguais, o auumento é de 15%.
salario = float(input('Informe o salario: '))

if salario > 1250.00:
    aumento = salario + (salario * 10 / 100)
    print('Seu salario que era R${:.2f}, com o aumento de 10% passa a ser de R${:.2f}'.format(salario, aumento))
else:
    aumento = salario + (salario * 15 / 100)
    print('Seu salario que era R${:.2f}, com o aumento de 15% passa a ser de R${:.2f}'.format(salario, aumento))