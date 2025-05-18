valor_1 = int(input('Digite o prineiro valor: '))
valor_2 = int(input('Digite o segundo valor: '))
valor_3 = int(input('Digite o terceiro vzlor: '))
valor_4 = int(input('Digite o quarto valor: '))
valores = valor_1, valor_2, valor_3, valor_4
print(valores)
nove = par = 0 
for valor in valores:
    if 9 == valor:nove+=1 
    print(f'O número nove apareceu {nove} vezes')
    if 3 == valor:print(f'o número treis apareceu na pocição {valores.index(3)+1}')
else:print('O número treis não foi digitado ')
   
# print(f'apareceu {} números pares')

# A) Quantas vezes apareceu o valor 9.

# B) Em que posição foi digitado o primeiro valor 3.

# C) Quais foram os números pares.