from random import shuffle
aluno_1 = input('Aluno 1: ')
aluno_2 = input('Aluno 2: ')
aluno_3 = input('Aluno 3: ')
aluno_4 = input('Aluno 4: ')
alunos = [aluno_1, aluno_2, aluno_3, aluno_4]
shuffle(alunos)
print(alunos)