import pygame
from os import path
import os

from config import WIDTH, HEIGHT, FPS, WHITE, BLACK, BLUE

BIRD_WIDTH = 90
BIRD_HEIGHT = 130

pygame.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tappy Wings')



font = pygame.font.Font('assets/fonte/fonte_principal.ttf', 25)

image = pygame.image.load('assets/img/fase1.png').convert()
background = pygame.transform.scale(image, (WIDTH, HEIGHT))

bird = pygame.image.load('assets/img/idle/frame-1.png').convert_alpha()
bird = pygame.transform.scale(bird, (BIRD_WIDTH, BIRD_HEIGHT))

def aminacao_passaro(pasta): 
    frames = []
    for nome_arquivo in sorted(os.listdir(pasta)):
        caminho = os.path.join(pasta, nome_arquivo)
        imagem = pygame.image.load(caminho).convert_alpha()
        frames.append(imagem)
    return frames

class passaro(pygame.sprite.Sprite):
    def __init__(self, frames):
        pygame.sprite.Sprite.__init__(self)

        self.frames = frames
        self.frame_index = 0
        self.image = pygame.transform.scale(self.frames[self.frame_index], (BIRD_WIDTH, BIRD_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.centerx = 240
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 1000 // fps_animacao
        self.speedx = 0
        self.speedy = 0
        self.gravity = 0.005 
        self.jump_strength = -0.9 # ----- É possível deixar mais lento?

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame_index = (self.frame_index + 1) % len(self.frames)
            self.image = pygame.transform.scale(self.frames[self.frame_index], (BIRD_WIDTH, BIRD_HEIGHT))

        if self.speedy > 10:
            self.speedy = 10

        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.speedy = self.jump_strength
        else:
            self.speedy += self.gravity

        self.rect.y += self.speedy

        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
            self.speedy = 0


fps_animacao = 10
pasta_animacao = 'assets/img/idle'
frames = aminacao_passaro(pasta_animacao)
indice_frame = 0
tempo_ultimo_frame = pygame.time.get_ticks()

player = passaro(frames)
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

clock = pygame.time.Clock()
game = True
start = True

start_ticks = pygame.time.get_ticks()

fundo_estado = "manha"

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            start = True
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            player.speedy = player.jump_strength

    agora = pygame.time.get_ticks()
    if agora - tempo_ultimo_frame > 1000 // fps_animacao:
        indice_frame = (indice_frame + 1) % len(frames)
        tempo_ultimo_frame = agora

    all_sprites.update()

    segundos_totais = (pygame.time.get_ticks() - start_ticks) // 1000
    minutos = segundos_totais // 60
    segundos = segundos_totais % 60
    texto_tempo = font.render(f"Tempo: {minutos:02}:{segundos:02}", True, BLUE)

    window.blit(background, (0, 0))
    all_sprites.draw(window)
    window.blit(texto_tempo, (10, 10))
    pygame.display.update()

pygame.quit()