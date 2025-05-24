soma = 0
con = 0
for c in range(1, 7):
    valor = int(input('Digite {}° valor: '.format(c)))
    if valor % 2 == 0:
        soma += valor
        con += 1
print('Emtre os valores digitado {} são PARES, a soma entre eles PARES {} '.format(con, soma))


