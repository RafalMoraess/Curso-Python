# ano atual
from datetime import datetime as dt
ano_atual = dt.now().year

menor_de_idade = 0
maior_de_idade = 0


for pesoas in range(1, 7+1):
    ano_nacimento =int(input('Em qual ano a {}ª pessoa nasceu? '.format(pesoas)))
    if ano_atual - ano_nacimento < 18:
        menor_de_idade += 1
    else:
       maior_de_idade += 1
print('Estamos no ano de ', ano_atual)
print('Ao todo tiemos {} pessoas maiores de idade'.format(maior_de_idade))
print('E também tivemos {} pessoas menores de idade'.format(menor_de_idade))