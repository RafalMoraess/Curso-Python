# ano atual
from datetime import datetime as dt
ano_atual = dt.now().year


# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta 
ano_nacimento = int(input('Ano em que o atleta naceu: '))

idade = ano_atual - ano_nacimento
print('Você naceu em {} e tem {} anos agora em {} '.format(ano_nacimento, idade, ano_atual))
#  – Até 9 anos: MIRIM
if idade < 9:
    print('Você é um atleta \033[31mMIRIM\033[m')
# – Até 14 anos: INFANTIL
elif 9 >= idade and idade < 14:
    print('Você é um atleta \033[33mIMFANTIL\033[m')
# – Até 19 anos: JÚNIOR
elif 14 >= idade and idade < 19:
    print('Você é um atleta \033[36mJÚNIOR\033[m')
# – Até 25 anos: SÊNIOR
elif 19 >= idade and idade < 25:
    print('Você é um atleta \033[32mSÊNIOR\033[m')
# – Acima de 25 anos: MASTER
elif idade > 25:
    print('Você e um atleta \033[35MASTER\033[m')