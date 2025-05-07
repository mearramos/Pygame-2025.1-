import pygame
from os import path
import os


from config import WIDTH, HEIGHT, FPS, WHITE, BLACK

pygame.init()

# ----- Gera tela principal
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Nome do jogo')

image = pygame.image.load('assets/sky.png').convert()
background = pygame.transform.scale(image, (WIDTH, HEIGHT))


titulo = "Nome do jogo"
Mensagem = "Aperte ENTER para iniciar"

game = True

while game:

    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT: # ------ Se o evento for um click no "X"
            game = False              # ------ Sai do jogo

    window.blit(background, (0, 0))
    pygame.display.update()

pygame.quit()

