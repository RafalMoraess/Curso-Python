from time import sleep as sp
#  Crie um programa que leia dois valores
v1 = int(input('Digite o 1º valor: '))
v2 = int(input('Digite o 2º valor: '))


# Seu programa deverá realizar a operação
# solicitada em cada caso.

    # e mostre um menu na tela:
print('''\033[mSuas opções:
[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa
''')
maior = 0
op = 0
op = int(input('Sua opção: '))

# [ 5 ] sair do programa
while op != 5:
    sp(1)

    # [ 1 ] somar
    if op == 1:
        print(f'A soma entre \033[33m{v1}\033[m e \033[32m{v2}\033[m = {v1+v2}')

        # [ 2 ] multiplicar
    elif op == 2:
        print(f'Multiplicando o valor \033[33m{v1}\033[m X \033[32m{v2}\033[m = {v1*v2}')

        # [ 3 ] maior
    elif op == 3:
        if v1 > v2:
            maior = v1
        elif v2 > v1:
            maior = v2
            print(f'O maior entre \033[33m{v1}\033[m e \033[32m{v2}\033[m é {maior}')
        else:
            print(f'Entre \033[33m{v1}\033[m e \033[32m{v2}\033[m não EXISTE MAIOR')

            # [ 4 ] novos números
    elif op == 4:
        v1 = int(input('Digite o 1º valor: '))
        v2 = int(input('Digite o 2º valor: '))
    
    else:
        print('\033[31mDigito invalido,\033[m TENTE NOVAMENTE ')
    
        # e mostre um menu na tela:
    sp(1)
    print('=-='*15)
    print('''Suas opções:
[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa
''')
    op = int(input('Escolha outra opção: '))

print('Fim')