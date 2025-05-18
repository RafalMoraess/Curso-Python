from ex115.lib.interface import *
from time import sleep as sp
from ex115.lib.arquivos import *

arq = 'cadastro_de_pessoas_ex115.txt'

if not arquivoExisre(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['\033[34mVer pessoas cadastradas', 'Cadastrar novas pessoa', 'Sair do Sistema\033[m'])
    if resposta == 1:
        # Opção de lista o conteudo de um arquivo 
        lerArquivo(arq)
    elif resposta == 2:
        # Opção de cadastro uma nova pessoa
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo...')
        sp(2)
        break
    else:
        print('\033[31mERRO: Por favor, digite um valor valido!\033[m')
    sp(1)
print('FIM!')
