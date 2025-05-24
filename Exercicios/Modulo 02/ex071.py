print('Banco')
print('='*30)
valor = int(input('valor que serár liberado:'))
cel = 50
totalcel = 0
total = valor
while True:
    if total >= cel:
        total -= cel
        totalcel +=1
    else:
        if totalcel > 0 :
            print(f'total de {totalcel}  celulas de R${cel}')
        if cel == 50:
            cel = 20
        elif cel == 20:
            cel = 10
        elif cel == 10:
            cel = 1
        totalcel = 0
        if total == 0:
            break