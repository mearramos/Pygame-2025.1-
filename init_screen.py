import pygame
from os import path
import os

from config import WIDTH, HEIGHT, FPS, WHITE, BLACK, BLUE

pygame.init()

# ----- Gera tela principal
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tappy Wings')

# ----- Carrega e ajusta fundo
image = pygame.image.load('assets/img/sky.png').convert()
background = pygame.transform.scale(image, (WIDTH, HEIGHT))

logo = pygame.image.load('assets/img/logo_tappy_wings.png').convert_alpha() #Logo para teste, substituição após término do design. 16/05.
logo_rect = pygame.transform.scale(logo, (WIDTH//2, HEIGHT//2 - 40))


# ----- Define fonte e mensagens
font = pygame.font.Font('assets/fonte/fonte_principal.ttf', 34)
titulo = "Tappy Wings"
mensagem = "Aperte ENTER para iniciar"

text_title = font.render(titulo, True, BLUE)
text_msg = font.render(mensagem, True, BLUE)

# ----- Centraliza textos na tela
title_rect = text_title.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 40))
msg_rect = text_msg.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 260))


# ----- Loop da tela inicial
game = True
start = False

while game and not start:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            start = True

    window.blit(background, (0, 0))
    # window.blit(text_title, title_rect)
    window.blit(text_msg, msg_rect)
    window.blit(logo, (150, 150))
    pygame.display.update()

pygame.quit()

