# Melhore o desafio 61, perguntando para o usuario se ele quer mostrar mais alguns termos. O programa encerrar quando ele disser que quer mostrar 0 termos.

primeiro = int(input('Digite o número inicial: '))
razao = int(input('Digite a razão: '))
termos = 1 

while termos != 0:
    termos = int(input('\nQuantos termos deseja exibir? Digite 0 para sair. '))
    mostrar = primeiro + (termos - 1) * razao # calculo enesimo termo da PA
    while mostrar >= primeiro:
        print(primeiro, end=' -> ')
        primeiro += razao
print('ACABOU')