import sys
import pygame
from bullet import Bullet

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

def update_screen(ai_settings, screen, ship, bullets):
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites(): 
        bullet.draw_bullet()
    ship.blitme()
        
    pygame.display.flip()