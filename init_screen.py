import pygame
from os import path
import os


# from config import WIDTH, HEIGHT, FPS, WHITE, BLACK

WIDTH = 1000  # Largura da tela
HEIGHT = 750  # Altura da tela
FPS = 30 # Frames por segundo

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

pygame.init()

# ----- Gera tela principal
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Nome do jogo')


titulo = "Nome do jogo"
Mensagem = "Aperte ENTER para iniciar"

game = True

while game:

    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT: # ------ Se o evento for um click no "X"
            game = False              # ------ Sai do jogo
    
    window.fill(BLACK)

    pygame.display.update()

pygame.quit()

