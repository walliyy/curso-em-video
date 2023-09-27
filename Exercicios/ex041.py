'''A confederaçao Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre a sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 25 anos: SENIOR
- Acima: MASTER'''
from datetime import date

anoAtual = date.today().year
nasc = int(input('Informe o ano de nascimento do atleta: '))
idade = anoAtual - nasc

if idade <= 9:
    print('O atleta tem {} anos e se encaixa na categoria MIRIM'.format(idade))
elif idade <= 14:
    print('O atleta tem {} anos e se encaixa na categoria INFANTIL'.format(idade))
elif idade <= 19:
    print('O atleta tem {} anos e se encaixa na categoria JÚNIOR'.format(idade))
elif idade <= 25:
    print('O atleta tem {} anos e se encaixa na categoria SÊNIOR'.format(idade))
elif idade > 25:
    print('O atleta tem {} anos e se encaixa na categoria MASTER'.format(idade))