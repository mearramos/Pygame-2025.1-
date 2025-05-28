if __name__ == "__main__":
    import pygame
    from init_screen import init_screen
    from game_screen import game_screen
    from config import WIDTH, HEIGHT, FPS, WHITE, BLACK, BLUE, DARK_BLUE, GREEN, DARK_GREEN
    from final_screen import final_screen
    from tutorial import tutorial_screen
   
    # ----- Define constantes para representar os diferentes estados do jogo
    INIT = 0
    GAME = 1
    QUIT = 2
    FINAL = 3
    TUTORIAL = 4

    # ----- Inicializa os módulos do Pygame
    pygame.init()
    pygame.mixer.init()

    # ----- Define tela cheia
    window = pygame.display.set_mode((WIDTH, HEIGHT))

    # ----- Gera tela principal
    pygame.display.set_caption('Tappy Wings')

    # ----- Variáveis de controle
    game = True
    state = INIT

    # ----- Loop principal do jogo, executa até o estado ser QUIT
    while state != QUIT:
        if state == INIT:
            state = init_screen(window)
        elif state == GAME:
            state = game_screen(window)
        elif state == FINAL:
            state = final_screen(window)
        elif state == QUIT:
            game = False
        elif state == TUTORIAL:
            state = tutorial_screen(window)
    pygame.quit()