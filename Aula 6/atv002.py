# Digite algo e imprima todas informações possiveis sobre essa informação
info = input('Digite alguma informação: ')

print(type(info), (info))
print('é alfanumerico? ', info.isalnum())
print('é alpha? ', info.isalpha())
print('é ASCII? ', info.isascii())
print('é decimal? ', info.isdecimal())
print('é digito? ', info.isdigit())
print('é infeidicavel? ', info.isidentifier())
print('é caixa baixa? ', info.islower())
print('é numero? ', info.isnumeric())
print('é imprimivel? ', info.isprintable())
print('é espaço? ', info.isspace())
print('é titulo? ', info.istitle())
print('é caixa alta? ', info.isupper())