import pygame
from os import path
import os
import random

# ----- Importa variáveis e constantes de configuração
from config import WIDTH, HEIGHT, FPS, WHITE, BLACK, BLUE, DARK_BLUE, RED, lose

# ----- Define os estados do jogo
INIT = 0
GAME = 1
QUIT = 2
FINAL = 3

# ----- Função principal da tela de jogo
def game_screen(window):
    clock = pygame.time.Clock()
    BIRD_WIDTH = 90
    BIRD_HEIGHT = 130

    # ----- Inicializa pygame e música
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("assets/sound/mushroom.mp3")
    pygame.mixer.music.play(-1)

    loser = pygame.mixer.Sound(lose)

    fundo_estado = "nivel_1" # ----- Define o estado inicial do jogo após o início
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Tappy Wings') # ----- Título da tela
    cano_x = WIDTH # ----- Posição inicial do cano
    velocidade = 0.5 # ----- Velocidade inicial do cano

    pipe_top = pygame.image.load("assets/img/new_obstacle_top.png")
    pipe_bottom = pygame.image.load("assets/img/new_obstacle_bottom.png")

    # ----- Cria máscaras para detecção de colisão
    mask_pipe_top = pygame.mask.from_surface(pipe_top)
    mask_pipe_bottom = pygame.mask.from_surface(pipe_bottom)

    pipe_width = pipe_top.get_width() # ----- Largura dos canos
    gap_pipe = 300 # ----- Distância entre canos

    pipe_x = WIDTH

    font = pygame.font.Font('assets/fonte/fonte_principal.ttf', 25) # ----- Fonte usada para texto

    # ----- Carrega fundo da fase 1
    image = pygame.image.load('assets/img/fase1.png').convert()
    background = pygame.transform.scale(image, (WIDTH, HEIGHT))

    # ----- Carrega imagem inicial do pássaro
    bird = pygame.image.load('assets/img/idle/frame-1.png').convert_alpha()
    bird = pygame.transform.scale(bird, (BIRD_WIDTH, BIRD_HEIGHT))

    # ----- Função para carregar os frames da animação do pássaro
    def aminacao_passaro(pasta): 
        frames = []
        for nome_arquivo in sorted(os.listdir(pasta)):
            caminho = os.path.join(pasta, nome_arquivo)
            imagem = pygame.image.load(caminho).convert_alpha()
            frames.append(imagem)
        return frames
    
    # ----- Classe do pássaro
    class passaro(pygame.sprite.Sprite):
        def __init__(self, frames):
            pygame.sprite.Sprite.__init__(self)

            self.frames = frames
            self.frame_index = 0
            self.image = pygame.transform.scale(self.frames[self.frame_index], (BIRD_WIDTH, BIRD_HEIGHT))
            self.rect = self.image.get_rect()
            self.rect.centerx = WIDTH//2
            self.rect.bottom = HEIGHT//2
            self.speedx = 0
            self.last_update = pygame.time.get_ticks()
            self.frame_rate = 1000 // fps_animacao
            self.speedx = 0
            self.speedy = 0
            self.gravity = 0.004491 # ----- Gravidade
            self.jump_strength = -0.7 # ----- Força do pulo

            self.mask = pygame.mask.from_surface(self.image)

        # ----- Atualiza posição e animação do pássaro
        def update(self):
            now = pygame.time.get_ticks()
            if now - self.last_update > self.frame_rate:
                self.last_update = now
                self.frame_index = (self.frame_index + 1) % len(self.frames)
                self.image = pygame.transform.scale(self.frames[self.frame_index], (BIRD_WIDTH, BIRD_HEIGHT))
                self.mask = pygame.mask.from_surface(self.image)

            # ----- Limita a velocidade de queda
            if self.speedy > 10:
                self.speedy = 10

            # ----- Movimento horizontal
            self.rect.x += self.speedx
            if self.rect.right > WIDTH:
                self.rect.right = WIDTH
            if self.rect.left < 0:
                self.rect.left = 0

            # ----- Controle do pulo
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                self.speedy = self.jump_strength
            else:
                self.speedy += self.gravity

            # ----- Movimento vertical
            self.rect.y += self.speedy
            
            # ----- Limita o pássaro ao topo e base da tela
            # if self.rect.top < 0:
            #     self.rect.top = 0
            # if self.rect.bottom > HEIGHT:
            #     self.rect.bottom = HEIGHT
            #     self.speedy = 0

    # ----- Classe dos canos
    class Cano(pygame.sprite.Sprite):
        def __init__(self, image, x, y):
            super().__init__()
            self.image = image
            self.rect = self.image.get_rect(topleft=(x, y))
            self.mask = pygame.mask.from_surface(self.image)

        # ----- Move os canos para a esquerda
        def update(self):
            self.rect.x -= 0.5
            if self.rect.right < 0:
                self.rect.left = WIDTH

    # ----- Gera altura aleatória para os canos
    def gerar_altura():
        return random.randint(100, HEIGHT - gap_pipe - 100)

    altura_cano_cima = gerar_altura()

    fps_animacao = 10
    pasta_animacao = 'assets/img/idle'
    frames = aminacao_passaro(pasta_animacao)
    indice_frame = 0
    tempo_ultimo_frame = pygame.time.get_ticks()

    # ----- Cria o jogador e grupo de sprites
    player = passaro(frames)
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    clock = pygame.time.Clock()
    game = True
    start = True

    start_ticks = pygame.time.get_ticks() # ----- Tempo inicial

    fundo_estado = "nivel_1"

    # ----- Loop principal do jogo
    while game:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.QUIT:
                return QUIT
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    return QUIT

        agora = pygame.time.get_ticks()
        if agora - tempo_ultimo_frame > 1000 // fps_animacao:
            indice_frame = (indice_frame + 1) % len(frames)
            tempo_ultimo_frame = agora

        all_sprites.update()

        # ----- Calcula tempo de jogo
        segundos_totais = (pygame.time.get_ticks() - start_ticks) // 1000
        minutos = segundos_totais // 60
        segundos = segundos_totais % 60
        texto_tempo = font.render(f"{minutos:02}:{segundos:02}", True, DARK_BLUE)

        # ----- Muda para nível 2 e aumenta a velocidade
        if segundos >= 45 and not fundo_estado == "nivel_2" and not fundo_estado == "nivel_3":
            image = pygame.image.load('assets/img/fase2.png').convert()
            background = pygame.transform.scale(image, (WIDTH, HEIGHT))
            velocidade = 1.3
            pipe_top = pygame.image.load("assets/img/new_obstacle_top_n2.png")
            pipe_bottom = pygame.image.load("assets/img/new_obstacle_bottom_n2.png")
            fundo_estado = "nivel_2"

        # ----- Muda para nível 3 e aumenta a velocidade
        if (minutos == 1 and segundos >= 30) and not fundo_estado == "nivel_3":
            image = pygame.image.load('assets/img/fase3.png').convert()
            background = pygame.transform.scale(image, (WIDTH, HEIGHT))
            pipe_top = pygame.image.load("assets/img/new_obstacle_top_n3 (3).png")
            pipe_bottom = pygame.image.load("assets/img/new_obstacle_bottom_n3.png")
            velocidade = 1.8
            fundo_estado = "nivel_3"
        
        cano_x -= velocidade # ----- Move os canos

        # ----- Reposiciona os canos quando saem da tela
        if cano_x + pipe_width < 0:
            cano_x = WIDTH
            altura_cano_cima = gerar_altura()

        window.fill((135, 206, 250))  # ----- Cor de fundo

        # ----- Calcula posições dos canos
        pos_cano_cima = (cano_x, altura_cano_cima - pipe_top.get_height())
        pos_cano_baixo = (cano_x, altura_cano_cima + gap_pipe)

        # ----- Desenha fundo, sprites e canos
        window.blit(background, (0, 0))
        all_sprites.draw(window)
        window.blit(pipe_top, pos_cano_cima)
        window.blit(pipe_bottom, pos_cano_baixo)
        window.blit(texto_tempo, (10, 10))

        # ----- Verifica colisões com canos
        offset_cima = (int(cano_x - player.rect.x), int(pos_cano_cima[1] - player.rect.y))
        offset_baixo = (int(cano_x - player.rect.x), int(pos_cano_baixo[1] - player.rect.y))

        colisao_cima = player.mask.overlap(mask_pipe_top, offset_cima)
        colisao_baixo = player.mask.overlap(mask_pipe_bottom, offset_baixo)

        if colisao_cima or colisao_baixo:
            loser.play()
            pygame.time.delay(1000)
            state = FINAL
            game = False

        if player.rect.top <= 0 or player.rect.bottom >= HEIGHT:
            loser.play()
            pygame.time.delay(1000)
            state = FINAL
            game = False

        # ----- Termina jogo após 2 minutos e 30 segundos
        if (minutos == 2 and segundos == 30):
            game = False
            state = FINAL

        pygame.display.update()

    return state