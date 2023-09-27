nome = str(input('Qual o seu nome? '))

if nome == 'Wallyson':
    print('Que nome bonito!')
elif nome == 'João' or nome == 'Ana':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Pedro Paulo Maria':
    print('Nome bem comum!')
else:
    print('Que porra de nome é esse?')
print('\033[1;42mQue bom te ver, {}!\033[m'.format(nome))