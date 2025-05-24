# Exercício Python 108: Adapte o código do desafio 
# 107, criando uma função adicional chamada moeda()
# que consiga mostrar os números como um valor monetário formatado.

import moedas02

# programa principal
dig = float(input('Preço: R$'))
print(f'{moedas02.moedas(dig)} + 10% = {moedas02.moedas(moedas02.aumentar(dig))}')
print(f'{moedas02.moedas(dig)} X 2 = R${moedas02.moedas(moedas02.dobro(dig))}')
print(f'{moedas02.moedas(dig)} % 2 = R${moedas02.moedas(moedas02.metade(dig))}')

