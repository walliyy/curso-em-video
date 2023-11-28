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

# Solução do professor
primeiro = int(input('Digite o número inicial da PA: '))
razao = int(input('Digite a razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(termo, end=' -> ')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('\nQuantos termos deseja exibir? Digite 0 para sair. '))
print(f'Progressão finalizada com {total} termos mostrados.')