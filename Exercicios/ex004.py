# Digite algo e imprima todas informações possiveis sobre essa informação
info = input('Digite alguma informação: ')

print('o valor é {} e tipo primitivo do valor é {}'.format(info, type(info)))
print('é alfanumerico? ', info.isalnum())
print('é alpha? ', info.isalpha())
print('é ASCII? ', info.isascii())
print('é decimal? ', info.isdecimal())
print('é digito? ', info.isdigit())
print('é infeidicavel? ', info.isidentifier())
print('é minusculo? ', info.islower())
print('é numero? ', info.isnumeric())
print('é imprimivel? ', info.isprintable())
print('é somente espaço? ', info.isspace())
print('esta capitalizado? ', info.istitle())
print('é maiuscula? ', info.isupper())
