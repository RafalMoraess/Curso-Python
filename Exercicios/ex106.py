c = ['\033[m', # Sem cor
     '\033[0,30,41m', # Vermelho
     '\033[0,30,42m', # Verde
     '\033[0,30,44m' # Azul
     ]
def lin(msg, cor):
    print(c[cor], end='')
    a = len(msg) + 4
    print('-'*a)
    print(f'{msg.center(a)}')
    print('-'*a)
    print(c[0], end='')
def ajuda(com):
    lin(f'Acessando o manual do comando \'{com}\'',3)
    help(com)
# programa principal
comando = ''
while True:
    lin('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        lin(f'Finalizando volte sempre', 1)
        break
    else:
        ajuda(comando)