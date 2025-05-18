preso = float(input('Digite o preço do produto: R$'))
desconto = preso * 0.05
valor = preso - desconto
print('O desconto de {} é de 5% que é R${:.2f}'.format(preso, valor))