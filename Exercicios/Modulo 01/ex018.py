from math import sin, cos, tan, radians
an = float(input('Digite o valor do angulo: '))
s = sin(radians(an)) 
c = cos(radians(an))
t = tan(radians(an))
print('O SENO do angulo é de {:.2f}'.format(s))
print('O COSSENO do angulo é de {:.2f}'.format(c))
print('O TANGENTE do angulo é de {:.2f}'.format(t))

# desafio fazer novamente no futuro