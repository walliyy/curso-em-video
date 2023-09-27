for c in range(0, 7, 2): #conta de 2 em 2
    print('Oi')
for c in range(6, 0, -1): #conta pra tras
    print('Oi de novo')

i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

for c in range(i, f+1, p):
    print(c) 