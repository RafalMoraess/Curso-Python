salario = float(input('Digete seu salário: '))
if salario >= 1250:
    print('teve um aumento de 10% o seu novo salário é R${}'.format(salario*0.10+salario))
else:
    print('teve um aumento de 15% o seu novo salário R${}'.format(salario*0.15+salario))