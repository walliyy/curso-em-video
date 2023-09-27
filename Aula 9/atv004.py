# Crie um programa que leia o nome de de uma cidade e diga se ela começa ou não com o nome "Santo"
c = str(input('Digite o nome da sua cidade: ')).strip()
print(('santo' in (c.lower().split()[0])))
print(c[:5].lower() == 'santo')  