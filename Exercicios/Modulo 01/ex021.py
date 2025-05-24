import pygame
import time
import os

# Verifica se o arquivo existe
if not os.path.exists('ex021.mp3'):
    print("Arquivo 'ex021.mp3' não encontrado.")
else:
    pygame.init()
    pygame.mixer.init()  # Inicializa o mixer separadamente (boa prática)
    pygame.mixer.music.load('ex021.mp3')
    pygame.mixer.music.play()

    # Espera a música terminar
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

