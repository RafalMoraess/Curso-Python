from datetime import datetime
ano_atual = datetime.now().year
ano = int(input('Ano de nacimento do jovem:\033[32m '))
alistar = 17 
idade = ano_atual - ano 
print('\033[mQuem naceu em {} tem {} anos em {}'.format(ano, idade, ano_atual))
if idade > alistar:
    print('\033[m\033[31mJá passou do ano do alistamento -{} anos\033[m!!!'.format(idade-alistar))
elif idade < alistar:
    print('\033[34mFalta {} anos para você se alistar\033[m!!!'.format(idade-alistar))
elif idade == alistar:
    print('\033[32mVocê está no ano certo para o alistamento militar você tem {} anos\033[m!!!'.format(alistar))
else:
    print('\033[31m ano invalido\033[m!')
