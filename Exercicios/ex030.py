# digitar um número inteiro
num = int(input('Digite um número inteiro: '))
numero = num % 2
if numero == 0:
    print('o número digitado foi {} e ele é PAR'.format(num))
else:
    print('o numero digitado foi {} e ele é IMPA'.format(num))
