def linha():
    print('-'*42)

def cabecalho(msg):
    linha()
    print(f'{msg}'.center(42))
    linha()

def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    linha()
    num = leiaint('\033[32mSua opção: \033[m')
    return num

def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
            return n
        except ValueError:
            print('\033[31mERRO: Por favor, Digite o número inteiro corretamente!\033[m')
        except KeyboardInterrupt:
            print('\033[31mERRO:O úsuario interrompeu o sistema!\033[m')
            break
