from math import ceil

n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
media = (n1+n2)/2
print('Notas de {} e {}, a media do alino é {}'.format(n1, n2, media))
if media < 5:
    # media menor que 5
    print('\033[31mREPROVADO\033[m')
    # media maior que 5 e menor que 7
elif 7> media >= 5.0:
    print('\033[33mRECUPERAÇÃO\033[m')
    # media maior ou igual a 7
elif media >= 7:
    print('\033[32mAPROVADO\033[m')