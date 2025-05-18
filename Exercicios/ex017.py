op = float(input('Conprimento do cateto oposto: '))
adj = float(input('Comprimento do cateto adjacent: '))
h = ((op**2)+(adj**2))**(1/2)
print('A hipotenusa vale {:.1f}'.format(h))


# OU



from math import hypot
o = float(input('Comprimento do cateto oposto: '))
ad = float(input('Comprimento do cateto adjacent: '))
h = hypot(o, ad)
print('A hipotenusa vale {}'.format(h))