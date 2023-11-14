# Crie um programa que leia vários numeros inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final mostre quantos numeros foram digitados e qual foi a soma entre ele (desconsiderando o flag)
soma = 0
qntd = 0
num = 0

while num != 999:
    num = int(input('Digite um numero [999 - sair]: '))
    if num != 999:
        soma += num
        qntd += 1
print(f'Você digitou {qntd} numeros e a soma deles é igual a {soma}!')