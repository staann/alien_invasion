import sys
import pygame
from bullet import Bullet
from alien import Alien

#Responde a eventos de pressionamento de teclas e de mouse
def check_keydown_events(event, ai_settings, screen, ship, bullets): 
    #"""Responde a pressionamentos de tecla."""
    if event.key == pygame.K_RIGHT: 
        ship.moving_right = True 
    elif event.key == pygame.K_LEFT: 
        ship.moving_left = True
    elif event.key == pygame.K_SPACE: # Cria um novo projétil e o adiciona ao grupo de projéteis 
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
    elif event.key == pygame.K_q: 
        sys.exit()  #fecha o jogo quando pressionado Q


def check_keyup_events(event, ship): 
    #Responde a solturas de tecla.
    if event.key == pygame.K_RIGHT: 
        ship.moving_right = False 
    elif event.key == pygame.K_LEFT: 
        ship.moving_left = False

def check_events(ai_settings, screen, ship,bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()

        elif event.type == pygame.KEYDOWN:  #KEYDOWN é uma evento sempre que uma tecla é pressionada
            check_keydown_events(event,ai_settings, screen, ship, bullets) 

        elif event.type == pygame.KEYUP: 
            check_keyup_events(event, ship)

def create_fleet(ai_settings, screen, aliens): #"""Cria uma frota completa de alienígenas."""
    # Cria um alienígena e calcula o número de alienígenas em uma linha # Oespaçamento entre os alienígenas é igual à largura de um alienígena u
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    # Cria a primeira linha de alienígenas y 
    for alien_number in range(number_aliens_x): # Cria um alienígena e o posiciona na linha z
        alien = Alien(ai_settings, screen) 
        alien.x = alien_width + 2*alien_width*alien_number 
        alien.rect.x = alien.x 
        aliens.add(alien) 


def update_screen(ai_settings, screen, ship, aliens, bullets):
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites(): 
        bullet.draw_bullet()
    ship.blitme()
    #alien.blitme()
    aliens.draw(screen)
        
    pygame.display.flip()