from time import sleep as sp
print('GERADOR DE PA')
print('-=' * 10)
primeiro = int(input('primeiro termo: '))
razão = int(input('razão: '))
tm = primeiro
cont = 1
while cont <= 10:
    print(f'{tm} -> ', end= '')
    tm += razão
    cont += 1
print('Fim')