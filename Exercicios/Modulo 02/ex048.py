som = 0
comn = 0
for num in range (1, 501, 2):
    if num % 3 == 0:
        som = num + som
        comn = comn + 1
print('Valor da soma de todos os números multiplos de 3:', som)
print('Quantas vezes forão somados os multiplos de 3:',comn)
