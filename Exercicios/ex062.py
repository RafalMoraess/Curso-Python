from time import sleep as sp
print('GERADOR DE PA')
print('-=' * 10)
primeiro = int(input('primeiro termo: '))
razão = int(input('razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} -> ', end= '')
        termo += razão
        cont += 1
    print('Pausa')
    mais = int(input('Quanto você deseja mostrar mais: '))
print(f'Progressão finalizada com {total} termos mostrado!')
