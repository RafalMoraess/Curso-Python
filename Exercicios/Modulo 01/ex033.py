a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
c = int(input('Digite outro número: '))
# Verificando Menor 
menor = a
if b < a and b < c:
    print('O menor número é {}'.format(b))
if c < a and c < b:
    print('O menor número é {}'.format(c))
if a < b and a < c:
    print('O menor nómero é {}'.format(a))
#  Verificando Maior 
maior = a
if a > b and a > c:
    print('O maior número é {}'.format(a))
if b > a and b > c:
    print('O maior número é {}'.format(b))
if c > a and c > b:
    print('O mair número é {}'.format(c))
