# PERGUNTAR COPRIMENTO 3 VS PARA FAZER UM TRIANGULO
cores = {'azul': '\033[34m',
        'limpa': '\033[m',
        'amarelo':'\033[33m',
        'verde': '\033[32m',
        'vermelho': '\033[31m'}

print('=-=-' * 15)
print('Analizando Triangulo...')
print('=-=-' * 15)
r1 = float(input(f'{cores['azul']}Comprimento da reta 1:{cores['amarelo']} '))
r2 = float(input(f'Comprimento da reta 2:{cores['verde']} '))
r3 = float(input(f'Comprimento da reta 3: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(f'{cores['verde']}Com o comprimento digitado TEM COMO forma um triangulo!!!{cores['limpa']}')
else:
    print(f'{cores['vermelho']}Com o comprimento digitado NÃO TEM COMO forma um triangulo!!!{cores['limpa']}')
