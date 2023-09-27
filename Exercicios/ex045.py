# Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep
pc = randint(1, 3)
eu = int(input('Selecione uma das opções abaixo: \n'
               '1 - Pedra \n'
               '2 - Papel \n'
               '3 - Tesoura \n'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('-=' * 15)
if pc == 1 and eu == 2:
    print('\033[4;36mComputador\033[m escolheu pedra')
    print('\033[4;36mVocê\033[m escolheu papel')
    print('\033[4;36mVocê\033[m venceu!')
elif pc == 1 and eu == 3:
    print('\033[4;36mComputador\033[m escolheu pedra')
    print('\033[4;36mVocê\033[m escolheu tesoura')
    print('\033[7;35mComputador\033[m ganhou!')
elif pc == 2 and eu == 1:
    print('\033[4;36mComputador\033[m escolheu papel')
    print('\033[4;36mVocê\033[m escolheu pedra')
    print('\033[7;35mComputador\033[m ganhou!')
elif pc == 2 and eu == 3:
    print('\033[4;36mComputador\033[m escolheu papel')
    print('\033[4;36mVocê\033[m escolheu tesoura')
    print('\033[4;36mVocê\033[m venceu!')
elif pc == 3 and eu == 1:
    print('\033[4;36mComputador\033[m escolheu tesoura')
    print('\033[4;36mVocê\033[m escolheu pedra')
    print('\033[4;36mVocê\033[m venceu!')
elif pc == 3 and eu == 2:
    print('\033[4;36mComputador\033[m escolheu tesoura')
    print('\033[4;36mVocê\033[m escolheu papel')
    print('\033[7;35mComputador\033[m ganhou!')
else:
    print('\033[4;36mAmbos escolheram a mesma opção!\033[m')
    print('\033[7;35mEmpate!\033[m')
print('-=' * 15)