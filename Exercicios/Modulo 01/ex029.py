# ler a velocidade do carro 
velocidade = float(input('Qual é a velocidade do carro? '))

if velocidade > 80.0:
    print('Você foi MULTADO por exeder limite de segurança que é 80km/n, valor da multa será de R${}'.format((velocidade-80)*7))
else:
    print('Tenha um bom dia! Dirija com segurança!')