media = cont = maior = menor = 0
while True:
    num = int(input('Digite um número: '))
    cont += 1
    para = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    media += num
    if cont == 1:
        maior = menor = num
    if maior < num:
            maior = num
    if menor > num:
            menor = num    
    if para == 'S':
        continue
    else:
        break
media = media/cont
print(f'Você digitou {cont} números e a média foi {media}\n e o maior número digitado foi {maior}\n e o menor foi {menor}')