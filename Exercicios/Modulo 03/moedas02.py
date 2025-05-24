def aumentar(num=0):
    p = 0.10
    r = p * num
    pp = r + num
    return pp
    
def dobro(num=0):
    d = 2 * num
    return d
    
def metade(num=0):
    m = num / 2
    return m

# def diminuir(num)

def moedas (preco=0, moedas='R$'):
    return f'{moedas}{preco:.2f}'.replace('.',',')

def resumo(x):
    print('-'*30)
    print('Rusumo de valor'.center(30))
    print('-'*30)
    print(f'analizando valor {moedas(x)}')
    print(f'{moedas(x)} + 10% = \t{moedas(aumentar(x))}')
    print(f'{moedas(x)} X 2 =   \t{moedas(dobro(x))}')
    print(f'{moedas(x)} % 2 =   \t{moedas(metade(x))}')