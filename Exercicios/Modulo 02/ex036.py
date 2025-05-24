# Pergunte o valor da casa,
casa = float(input('Digite o valor da casa:\033[32m '))
#  o salário do comprador
salario = float(input('\033[mDgite o valor do salario:\033[4;32;43m '))
# e em quantos anos ele vai pagar
anos = float(input('\033[mDigite o tempo em anos que será completamente pago:\033[32m  '))
# . A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
meses = anos * 12
prestaçao= casa / meses
salario_2 = salario * 30 / 100
if salario_2 <= prestaçao:
    print('\033[mA prstação será de {:.2f} o empréstimo foi \033[32mACEITO\033[m!!!'.format(prestaçao))
else:
    print('\033[mA pretação será de {:.2f} o empréstimo foi \033[31mNEGADO\033[m!!!'.format(prestaçao))