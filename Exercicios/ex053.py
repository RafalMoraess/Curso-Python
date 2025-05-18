
#Perguntar um nome, negar espaços externos, todas as letras em maiuscula!!!
frase = str(input('Digite seu nome: ')).strip().upper()

# separa o nome perguntado por palavras 
palavra = frase.split()

# junta cada palavra do nome perguntado
junto = ''.join(palavra)

'''# variavel para inverter o nome ná nome
# inverter = ''

# ir da ultima letra até a primeira, que é 0 mais sempre tenque ir 1 amenos,
# que vai voltar no paso negativo -1
# (resumindo esse é o inverso do nome digitado)

 for letra in range(len(junto)- 1, -1, -1):
    inverter += junto[letra]'''

                    # ou
# variavel para inverter o nome ná nome digitado
inverter= junto[::-1]

print('O inverso de {} é {}'.format(junto, inverter))
if inverter == junto:
    print('temos um palíndromo!')
else:
    print('O nome digitada não é um palíndromo!')