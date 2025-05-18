dias = float(input('Quantos dia alugado? '))
km = float(input('Quanto km rodados? '))
custo_dias = 60 * dias
custo_km = 0.15 * km
total = custo_dias + custo_km
print('O total que deverar ser pago é de {:.2f}'.format(total))
