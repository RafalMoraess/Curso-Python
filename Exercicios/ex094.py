# Exercício Python 094: Crie um programa que leia nome,
# sexo e idade de várias pessoas,
dados = [] 
mulheres = []
cont = t_idades = m = 0

while True:
    pessoas = {}
    pessoas['Nome'] = str(input('Nome: ')).capitalize()
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]

    while sexo not in 'MF':
        sexo = str(input('Por favor, digite apenas [M/F]: ')).upper().strip()[0]
        

    pessoas['Sexo'] = sexo
    pessoas['Idade'] = int(input('Idade: '))
    
    cont += 1 # (A)
    
    t_idades += pessoas['Idade'] # (B)

    if pessoas['Sexo'] in 'F':
        mulheres.append(pessoas)
        m +=1 # (C)

    ops = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    while ops not in 'SN':
        ops = str(input('\033[31mERRO\033[m digito invalido, quer continuar [S/N]')).strip().upper()[0]
    if ops in 'N':break

    dados.append(pessoas)
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre:
print('\033[32m-=-\033[m'*20)

# A) Quantas pessoas foram cadastradas
print(f'Foram cadastrada {cont} pessoas') if cont > 1 else print(f'Foram cadastrada {cont} pessoa')

# B) A média de idade 
media_idade = t_idades/cont
print(f'A media das idade é de {media_idade:.2f} anos.')

# C) Uma lista com as mulheres
if m > 0:
    print('Mulheres foram ',end= ' ')
    for pessoa in dados:
        if pessoa['Sexo'] == 'F':
            print(pessoas['Nome'])
else:
    print('Nem uma mulher no cadastrada')

# D) Uma lista de pessoas com idade acima da média
print('Pessoas com idade acima da média: ')
for pessoa in dados:
    if pessoa['Idade'] > media_idade:
        print(pessoa['Nome'], end=' ')
print('-=-=- ENSERRANDO -=-=-')