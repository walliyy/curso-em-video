# Faça um algoritmo que leia o salario de um funcionario e mostre seu novo salario, com 15% de aumento.
salario = float(input('Digite o salario do funcionario: '))

novoSalario = salario + (salario*0.15)
print('O novo preço do produto é R$ {:.2f}'.format(novoSalario))