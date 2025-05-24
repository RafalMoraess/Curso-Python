media = 0
total_idade = 0
velhoidade = 0
Nome = ''
Mu = 0

for p in range (1, 5):
    print('{}{}ª-PESSOA{}'.format('-'*5, p,'-'*5))
    nome = input('Nome: ')
    idade = float(input('idade: '))
    Sexo = input('Sexo [M/F]: ')
    total_idade += idade
    if p == 1 and Sexo in 'Mm':
        velhoidade = idade
        Nome= nome
    if Sexo in 'Mm' and idade > velhoidade:
        velhoidade = idade
        Nome = nome
    if Sexo in 'Ff' and idade < 20:
        Mu += 1
        
media = total_idade / 4
print('A media de idade do grupo é de {}'.format(media))
print('O homem mais velho de {} anos e seu nome é {}'.format(velhoidade, Nome))
print('Au todo são {} mulheres com menos de 20 anos'.format(Mu))


