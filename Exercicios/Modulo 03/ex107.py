# Exercício Python 107: Crie um módulo chamado moeda.py
# que tenha as funções incorporadas aumentar(),
# diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções. 

import moedas01

# programa principal
dig = float(input('Preço: R$'))
print(f'R${dig} + 10% = R${moedas01.aumentar(dig)}')
print(f'R${dig} X 2 = R${moedas01.dobro(dig)}')
print(f'R${dig} % 2 = R${moedas01.metade(dig)}')
