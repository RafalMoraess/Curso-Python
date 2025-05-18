num = som = cont = 0
num = int(input('Digite o número[999 para parar]: '))
while num != 999:
    som += num
    cont += 1
    num = int(input('Digite o número[999 para parar]: '))
print(f'Você digitou {cont} e a soma entre os números digitado é {som}')
print('\033[33mAcabou\033[m!!!')