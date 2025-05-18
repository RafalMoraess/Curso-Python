# Exercício Python 105: Faça um programa que tenha uma função notas() 
# que pode receber várias notas de alunos e vai retornar um dicionário
# com as seguintes informações:
# – Quantidade de notas
# – A maior nota 
# – A menor nota 
# – A média da turma  
# – A situação (opcional)

def notas(*n, sit=False):
    """Função = Essa função tem com finalidade exibir as notas dos alunos
    *n = uma variavel que ler variarias notas
    sit = mostar a situação dos alunos com baze na media
    return = representa a entrega de totos os dados """

    r = dict()
    r['total'] = len(n)
    r['menor'] = min(n)
    r['maior'] = max(n)
    r['média'] = sum(n)/len(n)
    if sit: 
        if r ['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r
# programa principal
resp = notas(5,5,5,4, sit=True)
print(resp)
# help(notas)