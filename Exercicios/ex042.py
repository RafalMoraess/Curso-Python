cores = {'azul': '\033[34m',
        'limpa': '\033[m',
        'amarelo':'\033[33m',
        'verde': '\033[32m',
        'vermelho': '\033[31m'}

print('=-=-' * 15)
print('Analizando Triangulo...')
print('=-=-' * 15)
l1 = float(input(f'{cores['azul']}Comprimento da reta 1:{cores['amarelo']} '))
l2 = float(input(f'Comprimento da reta 2:{cores['verde']} '))
l3 = float(input(f'Comprimento da reta 3: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print(f'{cores['verde']}Com o comprimento digitado TEM COMO forma um triangulo!!!{cores['limpa']}')

    if l1 == l2 and l2 == l3:
        print('Triangulo Equilatero, todos os lados são iguais!!!')
    elif l1 == l2 and l2 != l3 or l2 == l3 and l3 != l1 or l3 == l1 and l1 != l2:
        print('Triangulo Isósceles, porque dois lados são iguais!!!')
    else:
        print('Triangulo Escaleno, porque todos os lados são diferente!!!')
else:
    print(f'{cores['vermelho']}Com o comprimento digitado NÃO TEM COMO forma um triangulo!!!{cores['limpa']}')


# Poeria ter feito o Escaaleno primeiro que o Isósceles, seria bem mais rapido pois,
# a com paração do Isóscelestes é silples: l1 != l2 != l3 != l1 e depois colocava o else no final