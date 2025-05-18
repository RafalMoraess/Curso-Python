print('Sequência de Fibonacci')
print('-='*10)

num = int(input('Digite Quantos termaos será exibido: '))

t1 = 0 
t2 = 1

print(f'{t1} -> {t2} -> ', end= '')

f = 3

while f <= num:
    print(f'{t1 + t2} -> ', end = '')
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    f += 1
print('Fim!')

