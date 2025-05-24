salario = float(input('Digite o salario antigo: R$'))
almento = salario * 0.15
valor = salario + almento
print('Salário antigo R${} e o nova salário R${:.2f} '.format(salario, valor))