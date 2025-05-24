# 'Digite um nome completo'
nome = str(input('Digite seu nome: ')).strip()
print('Analisando ...')
# 'O nome completo com dodas as letras maiúsculas'
print('Seu nome em maiúscula {}'.format(nome.upper()))
# 'O nome completo comdas as letras minúsculas'
print('Seu nome em minúscula {}'.format(nome.lower()))
# 'Quantas letras tem ao todo (sem considerar espaços)'
print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
# 'Quantas letras tem o primeiro nome'
print('Sue primeiro nome tem {} letras'.format(nome.find(' ')))
        # OU
separa = nome.split()
print('Seu primeiro nome é {} e tem {} letras'.format(separa[0], len(separa[0])))