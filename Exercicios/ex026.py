# Faça um programa que leia uma  frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A"
# Em que posição ela aparece a primeira vez.
# Em que posição ela aparece a ultima vez.
frase = str(input('Digite uma frase: ')).strip()

print(frase.lower().count('a'))
print(frase.lower().find('a')+1)
print(frase.lower().rfind('a')+1) 