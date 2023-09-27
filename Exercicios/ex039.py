'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
- Se ele ainda vai ser alistar ao serviço militar.]
- Se é a hora de ser alistar.
- Se já passou do tempo de alsitamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo'''
from datetime import date

anoAtual = date.today().year

ano = int(input('Digite seu ano de nascimento: '))
idade = anoAtual - ano

if idade > 18:
    print('Você passou {} anos do idade de alistamento militar!'.format((anoAtual - ano)-18))
elif idade < 18:
   print('Ainda faltam {} anos para a realização alistamento militar!'.format(((anoAtual - ano)-18)*-1))
else:
    print('Você deve fazer o seu alistamento militar esse ano!') 