Sexo= 0

while Sexo != 1:
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if sexo == 'M':
        Sexo += 1
    if sexo == 'F':
        Sexo += 1
    else:
        print('Dados inválidos, porfavo, informe seu sexo!')
print('Sexo {}, regitrado com sucesso'.format(sexo))
