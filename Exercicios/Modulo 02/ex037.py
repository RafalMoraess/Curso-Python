n1 = int(input('Digite um Número: '))
print('Escolha uma das opções abaixo: ')
print('[ 1 ] Para binário ')
print('[ 2 ] Para octal ')
print('[ 3 ] para Hexadecimal ')
num = int(input('Digite um número inteiro: '))
if num == 1:
    print('\033[32mpara binario {}\033[m'.format(bin(n1)[2:]))
elif num == 2:
    print('\033[32mpara octal {}\033[m'.format(oct(n1)[2:]))
elif num == 3:
    print('\033[32mpara hexadecimal {}\033[m'.format(hex(n1)[2:]))
else:
    print('\033[31mOpção invalida tente novamente\033[m')
