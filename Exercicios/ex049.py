num = int(input('Digite um número para ver sua tabuada: '))
for c in range (1,11):
    print('{:2} X {:2} = {:2}'.format(num, c, c*num))