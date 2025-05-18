from time import sleep as sp
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
print('\033[32mClauculando seu índise de massa corporal\033[m...')
sp (2)
imc = peso / altura ** 2
print('Seu IMC é de {:.1f}'.format(imc))

# – IMC abaixo de 18,5: Abaixo do Peso
if imc < 18.5:
    print('Você está abaixo do pesso!!!')

# – Entre 18,5 e 25: Peso Ideal
elif 18.5 <= imc < 25.0:
    print('Você está no peso ideal!!!')

# – 25 até 30: Sobrepeso
elif 25.0 <= imc < 30.0:
    print('Cuidado está um pouco Acima do seu pesso ideal, Sobrepeso!!!')

# – 30 até 40: Obesidade
elif 30.0 <= imc < 40.0:
    print('Infelizmente vc está MUITO ACIMA do PESO, Obesidade')

# – Acima de 40: Obesidade Mórbida 
else:
    print('\033[31mInfelizmente vc está com, Obesidade Mórbida\033[m')