from random import randint
computador = randint(0, 10)
print('Tem te adivinhar o número que eu pensei de 0 á 10!')
acumulo = 0
num = -1
while not num == computador:
    num = int(input('Digite um número de 0 á 10: '))
    if num!=computador:
        acumulo+=1
    if num < computador:
        print('Mais alto')
    if num > computador:
        print('Mais baixo')
print('Você acertou o número que eu pense foi {}'.format(computador))
print('E você precisou de {} tentativa para acerta!'.format(acumulo))