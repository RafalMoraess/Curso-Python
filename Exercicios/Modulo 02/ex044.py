print('{}Loja=Moraes{}'.format('==='*3, '==='*3))
valor = float(input('Valor a ser pago: '))
print('Formas de pagamentos!!!')
print('[ 1 ] Para à vista, dinheiro/cheque')
print('[ 2 ] Para à vista no cartão')
print('[ 3 ] Para pagamento em até 2x no cartão') 
print('[ 4 ] Para 3x ou mais no cartão')
pagar = int(input('Digite: '))
if pagar == 1:
    print('Você recebeu um desconto de 10% valor a ser pago é de R${}'.format(valor - valor * 0.10))
elif pagar == 2:
    print('Você recebeu um desconto de 5% valor a ser pago é de R${}'.format(valor - valor * 0.05))
elif pagar == 3:
    print('Presso normal sem juros R${}'.format(valor))
else:
    print('Você obteve 20% de juros R${}'.format(valor + valor * 0.20))

