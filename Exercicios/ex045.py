from random import randint
from time import sleep as sp

lista = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
# faiz o computador escolher 1 item da lista aleatoriamente!!!
#print('O computador escolheu, {}'.format(lista[computador]))
print('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Qual é a sua jogada? '))
if jogador > 2:
    print('\033[31mValor invalido\033[m!!!!')
print('\033[32m-=\033[m' * 11)
print('Computador jogou {}'.format(lista[computador]))
print('Jogador jogou {}'.format(lista[jogador]))
print('\033[32m-=\033[m' * 11)
print('JÓ')
sp(1)
print('KEN')
sp(1)
print('PO!!!')
print('\033[33m-=\033[m' * 11)
print('O computador escolheu {}'.format(lista[computador]))
print('Você escolheu {}'.format(lista[jogador]))
if computador == 0: # Pedra
    if jogador == 0:
        print('\033[33mEMPATE\033[m!!!')
    elif jogador == 1:
        print('\033[32mVENCEDOR\033[m!!!')
    elif jogador == 2:
        print('\033[31mPERDEDOR\033[m!!!')
    else:
        print('\033[31mValor Invalido\033[m!!!')
elif computador == 1: # Papel
    if jogador == 0:
        print('\033[31mPERDEDOR\033[m!!!')
    elif jogador == 1:
        print('\033[33mEMPATE\033[m!!!')
    elif jogador == 2:
        print('\033[32mVENCEDOR\033[m!!!')
    else:
        print('\033[31mValor Invalido\033[m!!!')
elif computador == 2: # Tesoura
    if jogador == 0:
        print('\033[32mVENCEDOR\033[m!!!')
    elif jogador == 1:
        print('\033[31mPERDEDOR\033[m!!!')
    elif jogador == 2:
        print('\033[33mEMPATE\033[m!!!')
    else:
        print('\033[31mValor Imvalido\033[m!!!')
else:
    print('\033[31mValor Invalido\033[m')