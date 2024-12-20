import pygame.font


class Button:
    def __init__(self, ai_settings, screen, msg):
        #inicia atributos do botao
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # dimensoes e propriedades
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self.prep_msg(msg)

    def prep_msg(self, msg):
        #"rendeariza e centraliza a mensagem
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # Draw blank button, then draw message.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


class Dados:
    def __init__(self,ai_settings,screen,msg2,msg3,msg4):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.width, self.height = ai_settings.screen_width, 200
        self.button_color = (0, 0, 0)
        self.text_color = (255, 255, 0)
        self.font = pygame.font.SysFont(None, 42)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.bottom = self.screen_rect.bottom
        self.prep_msg2(msg2,msg3,msg4)
        #self.rect.center = self.screen_rect.center
        #self.prep_msg2(msg3)


    def prep_msg2(self,msg2,msg3,msg4):
        #"rendeariza e centraliza a mensagem
        self.msg_image = self.font.render(msg2, True, self.text_color, self.button_color)
        self.msg_image2 = self.font.render(msg3, True, self.text_color, self.button_color)
        self.msg_image3 = self.font.render(msg4, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image2_rect = self.msg_image2.get_rect()
        self.msg_image3_rect = self.msg_image3.get_rect()
        self.msg_image_rect.center = (683,750)   #esquerda =x; direita = y
        self.msg_image2_rect.center = (683,600)
        self.msg_image3_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
        self.screen.blit(self.msg_image2, self.msg_image2_rect)
        self.screen.blit(self.msg_image3, self.msg_image3_rect)
        