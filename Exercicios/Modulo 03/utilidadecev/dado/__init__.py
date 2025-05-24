def leiadinheiro(msg):
    validor = False
    while not validor:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada== '':
            print(f'\033[31mERRO: \'"{entrada}\"é um peço inválido!\033[m')
        else:
            validor = True
            return float(entrada)