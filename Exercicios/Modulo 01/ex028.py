from random import choice, randint
n = [1, 2, 3, 4, 5] # numero pensado
n1 = str(input('Eu pencei em um número de 1 a 5 adivinhe qual é: ')).strip()# adivinha
n2 = int(n1) # trasforma em número 
from time import sleep
print('Possesando...')
sleep(3) #fais demora 3 segundo para responder
if n2 == choice(n):
    print('Você acertou!')
else:
    print('Você errou!')
print('-=-=-'*20)


                    # ou
num_pensado = randint(1, 5) # numero pensado
n_2 = str(input('Eu pencei em outro número de 1 a 5 adivinhe qual é: ')).strip() # adivinha
num = int(n_2) # trasforma em númeroa
print('prossesando...')
sleep(3) #fais demora 3 segundo para responder
if num == num_pensado:
    print('Você acertou!!!')
else:
    print('Você errou!!!')
print('O número que eu pensei foi {}'.format(num_pensado))