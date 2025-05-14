import pygame
from os import path
import os

from config import WIDTH, HEIGHT, FPS, WHITE, BLACK, BLUE

pygame.init()

# ----- Gera tela principal
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tappy Wings')

# ----- Carrega e ajusta fundo
image = pygame.image.load('assets/sky.png').convert()
background = pygame.transform.scale(image, (WIDTH, HEIGHT))

logo = pygame.image.load('assets/logo_tappy_wings.png').convert()
logo_pos = pygame.transform.scale(logo, (400, 300))
logo_rect = logo.get_rect(center= (WIDTH//2, HEIGHT//2 - 40))

# ----- Define fonte e mensagens
font = pygame.font.Font('assets/fonte_principal.ttf', 34)
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
    window.blit(text_title, title_rect)
    window.blit(text_msg, msg_rect)
    window.blit(logo_pos, logo_rect)
    pygame.display.update()

pygame.quit()

