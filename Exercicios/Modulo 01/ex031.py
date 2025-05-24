distancia = str(input('Qual e a distacia da viagem em Km: ')).strip()
dis = float(distancia)
if dis <=200.0:
    print('A passagen custará R${}'.format(dis*0.50))
else:
    print('A passagen custará R${}'.format(dis*0.45))