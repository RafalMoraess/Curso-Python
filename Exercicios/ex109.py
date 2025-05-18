# Exercício Python 109: Modifique as funções que form criadas no desafio 107
# para que elas aceitem um parâmetro a mais, informando se o valor retornado
# por elas vai ser ou não formatado pela função moeda(),
# desenvolvida no desafio 108.

from moedas02 import moedas as mds, aumentar, dobro, metade

# programa principal
dig = float(input('Preço: R$'))
print(f'{mds(dig)} + 10% = {mds(aumentar(dig))}')
print(f'{mds(dig)} X 2 = R${mds(dobro(dig))}')
print(f'{mds(dig)} % 2 = R${mds(metade(dig))}')
