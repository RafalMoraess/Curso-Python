# LER UMA FRASE PELO TECLADO
nome = str(input('Digite seu nome: ')).upper().strip()

# QUANTAS LETRAS APARCE A LETRA 'A'
print('seu nome tem {} letas (a)'.format(nome.count('A')))

# EM QUAL POSIÇÃO APARECE A LETRA 'A'
print('a primeira letra (a) aparese na posição {}'.format(nome.find('A')+1))

# EM QUAL POSIÇÃO TERMINA A UTIMA LETRA 'A'
print('a ultima letra a aparece na posição {}'.format(nome.rfind('A')+1))