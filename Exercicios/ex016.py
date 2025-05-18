from math import trunc
valor_1 = float(input('Digite um valor: '))
print('O valor digitado foi {} e sua parte inteira é {}'.format(valor_1, trunc(valor_1)))

# OU

valor = float(input('Digite outro valor: '))
print('O valor digitado foi {} e sua parte inteira é {}'.format(valor, int(valor)))