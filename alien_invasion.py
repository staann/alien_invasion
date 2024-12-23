import pygame
from settings import Settings
from ship import Ship
from alien import Alien  
import game_functions as gf 
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from button import Dados
from pygame.sprite import Group
 

def run_game():
# Inicializa o jogo e cria um objeto para a tela
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    play_button = Button(ai_settings, screen, "Jogar")
    disciplina_button = Dados(ai_settings,screen, "Disciplina : FGA0158","Nome : Gustavo Choueiri","Matricula : 232014010",
'                                      Controles:                                    ',
'Espaço: atira ; Seta esquerda/direita : controla a nave')
    #matricula_buttom = Dados(ai_settings,screen, "Matricula : 232014010")
    #nome_buttom = Dados(ai_settings,screen, "Nome : Gustavo Choueiri")
    
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    ship = Ship(ai_settings,screen)
    bullets = Group()
    aliens = Group()
    #alien = Alien(ai_settings,screen)
    gf.create_fleet(ai_settings, screen,ship,aliens)

    #bg_color = (230, 230, 230)
# Inicia o laço principal do jogo 
    while True:
# Observa eventos de teclado e de mouse x 
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets) 
            #bullets.update() 
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)

        # Deixa a tela mais recente visível z
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button,disciplina_button)


run_game()