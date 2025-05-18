# import urllib
# import urllib.request
# try:
#     site = urllib.request.urlopen('https://www.pudim.com.br/')

# except urllib.error.URLError:
#     print('O site Pudim não está acessível no momento.')
# else:
#     print('Conse acessar o site Pudim com sucesso!')

import socket

def verificar_conexao():
    try:
        socket.create_connection(('www.google.com', 80), timeout=5)
        return True
    except (socket.timeout, socket.gaierror, socket.error):
        return False
    
# programa principal

if verificar_conexao():
    print('Conse acessar o site Pudim com sucesso!')
else:
    print('O site Pudim não está acessível no momento!')