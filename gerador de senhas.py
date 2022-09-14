from operator import length_hint
import random

print('Gerador de senhas')

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%¨&*(),.;?0123456789"

number = input('Quantas senhas deseja gerar?: ')
number = int(number)

length = input('Quantos caractéres terá sua senha?: ')
length = int(length)



print('\nAqui estão suas senhas: ')

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)

    