
# try: #Tentar
#     # Opção
#     # o que pode dar errado
#     n = int(input('Digite um número inteiro: '))

# # except Exception as erro: #Si der problema
# #                     # Falha
# #                     # se temtar as opção e falha o que vai acontecer
# #     print(f'\033[31mERRO, encontramos o erro de {erro.__class__}\033[m')

# except ValueError:
#     print(f'\033[31mERRO, não é permitido usar letras ou numero com pontos: \033[m')



#     # opcional

# else: # Si der certo
#     print(f'O número digitado foi {n}')

# finally:# Finalmente
#         #(Vai acontecer mesmo si der ERRADO ou Certo)
#     print('Volte sempre! Muito obrigado')

def leiaint(msg):
    while True:
        try:
            valor = int(input(msg))
            return valor
        except (ValueError):
            print('\033[31mERRO: Por favor, digite um número inteiro válido.\033[m')

        except (KeyboardInterrupt):
            print('\n\033[31mO usuário preferiu não informar o valor.\033[m')
            return 0
def leiafloat(msg):
    while True:
        try:
            valor = float(input(msg))
            return valor

        except ValueError:
            print('\033[31mERRO: Por favor, digite um número real de forma correta!\033[m')

        except KeyboardInterrupt:
            print('\033[31mO úsuario preferiu não digita!\033[m')
            return 0
# programa principal
for c in range (2):
    n = leiaint('Digite um número inteiro: ')
    r = leiafloat('Digite um número real: ')
    print(f'Valor digitado {n} e {r}')