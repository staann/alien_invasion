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
    def __init__(self,ai_settings,screen,msg2,msg3,msg4,msg5,msg6):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.width, self.height = ai_settings.screen_width, 200
        self.button_color = (0, 0, 0)
        self.text_color = (255, 255, 0)
        self.text_color2 = (0, 0, 255)
        self.font = pygame.font.SysFont(None, 42)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect_2 = pygame.Rect(0, 0, self.width, self.height)
        self.rect.bottom = self.screen_rect.bottom
        self.rect_2.center = self.screen_rect.center
        self.rect_2.top = self.screen_rect.top
        self.prep_msg2(msg2,msg3,msg4)
        self.prep_msg3(msg5,msg6)
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


    def prep_msg3(self,msg5,msg6):
        self.msg_image5 = self.font.render(msg5, True, self.text_color2, self.button_color)
        self.msg_image6 = self.font.render(msg6, True, self.text_color2, self.button_color)
        self.msg_image5_rect = self.msg_image5.get_rect()
        self.msg_image6_rect = self.msg_image6.get_rect()
        self.msg_image5_rect.center = self.rect_2.center
        self.msg_image5_rect.top = self.rect_2.top
        self.msg_image6_rect.center = self.rect_2.center
        self.msg_image6_rect.top = self.msg_image5_rect.bottom




    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
        self.screen.blit(self.msg_image2, self.msg_image2_rect)
        self.screen.blit(self.msg_image3, self.msg_image3_rect)
        self.screen.blit(self.msg_image5, self.msg_image5_rect)
        self.screen.blit(self.msg_image6, self.msg_image6_rect)
        