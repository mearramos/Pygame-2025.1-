import pygame
from os import path
import os
from config import mushroom
from config import WIDTH, HEIGHT, FPS, WHITE, BLACK, BLUE, DARK_BLUE, GREEN, DARK_GREEN, final_music

INIT = 0
GAME = 1
QUIT = 2
FINAL = 3
TUTORIAL = 4

def final_screen(window):
    clock = pygame.time.Clock()
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(final_music)
    pygame.mixer.music.play(-1)

    WIDTH_RET, HEIGH_RET = 800, 600
    cor_retangulo = (100, 149, 237, 180)
    ret_surf = pygame.Surface((WIDTH_RET, HEIGH_RET), pygame.SRCALPHA)
    pygame.draw.rect(ret_surf, cor_retangulo, ret_surf.get_rect(), border_radius=30)

    # ----- Gera tela principal
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Tappy Wings')

    # ----- Carrega e ajusta fundo
    image = pygame.image.load('assets/img/Fase1.png').convert()
    background = pygame.transform.scale(image, (WIDTH, HEIGHT))
    logo = pygame.image.load('assets/img/new_logo.png')
    birds_init = pygame.image.load('assets/img/birds_init.png').convert_alpha()

    # ----- Define fonte e mensagens
    font_titulo = pygame.font.Font('assets/fonte/fonte_principal.ttf', 50)
    font_msg = pygame.font.Font('assets/fonte/fonte_principal.ttf', 24)
    titulo = "fIM DE JOGO"
    mensagem = "ENTER para reiniciar"
    sair = "S para sair"
    tutorial = "T para tutorial"

    text_title = font_titulo.render(titulo, True, WHITE)
    text_msg = font_msg.render(mensagem, True, WHITE)
    text_sair = font_msg.render(sair, True, WHITE)
    text_tutorial = font_msg.render(tutorial, True, WHITE)

    # ----- Centraliza textos na tela
    title_rect = text_title.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 200))
    msg_rect = text_msg.get_rect(center=(WIDTH // 2 - 100, HEIGHT // 2 + 260))
    sair_rect = text_msg.get_rect(center=(WIDTH//2 - 100, HEIGHT//2 + 224))
    tutorial_rect = text_msg.get_rect(center=(WIDTH//2 - 100, HEIGHT//2 + 190))


    # ----- Loop da tela inicial
    game = True
    start = False
    state = INIT

    while game and not start:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return QUIT  
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    return QUIT
                if event.key == pygame.K_RETURN:
                    return GAME  
                if event.key == pygame.K_t:
                    return TUTORIAL


            
        x = (WIDTH - WIDTH_RET) // 2
        y = (HEIGHT - HEIGH_RET) // 2
        window.fill(BLUE)
        window.blit(background, (0, 0))
        window.blit(ret_surf, (x, y))
        window.blit(text_title, title_rect)
        window.blit(text_msg, msg_rect)
        window.blit(text_sair, sair_rect)
        window.blit(text_tutorial, tutorial_rect)
        window.blit(birds_init, (WIDTH//2 - 340, HEIGHT//2 - 200))
        pygame.display.update()
    return state

