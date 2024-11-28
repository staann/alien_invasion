import pygame
from settings import Settings
from ship import Ship
from alien import Alien  
import game_functions as gf 
from pygame.sprite import Group
 

def run_game():
# Inicializa o jogo e cria um objeto para a tela
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(ai_settings,screen)
    bullets = Group()
    aliens = Group()
    #alien = Alien(ai_settings,screen)
    gf.create_fleet(ai_settings, screen,aliens)

    #bg_color = (230, 230, 230)
# Inicia o laço principal do jogo 
    while True:
# Observa eventos de teclado e de mouse x 
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update() 
        # Deixa a tela mais recente visível z
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()