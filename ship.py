import pygame
#from settings import Settings

class Ship():
    
    def __init__(self,ai_settings,screen):
        #self.ai_settings = Settings()
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
#a cada nova espaçonave na parte inferior central da tela
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom 
        self.center = float(self.rect.centerx)
        self.moving_right = False  #FLAG DE MOVIMENTO
        self.moving_left = False
#Atualiza a posição da espaçonave de acordo com a flag de movimento    
    def update(self):
        self.rect.centerx = self.center
        
        if self.moving_right and self.rect.right < self.screen_rect.right: 
            self.center += self.ai_settings.ship_speed_factor
            #self.rect.centerx += 1   
            #if self.rect.bottomleft == self.screen_rect.bottomright:
                #self.rect.bottomleft == self.screen_rect.bottomleft
                #self.rect.centerx -= self.ai_settings.screen_width
                
        if self.moving_left and self.rect.left > 0: 
            self.center -= self.ai_settings.ship_speed_factor
            #self.rect.centerx -= 1
        



    def blitme(self):
        self.screen.blit(self.image, self.rect)