#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
print('-='*10)
print('\033[4m10 Termos de uma PA\033[m')
print('-='*10)
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
valor = termo + (10-1) * razao
for c in range (termo, valor + razao, razao):
    print(f'{c}', end=(' ->'))
print('ACABOU!!!')
