class Settings():
    def __init__(self):
        # Configurações da tela 
        self.screen_width = 1366
        self.screen_height = 768
        self.bg_color = (230, 230, 230)
        # Configurações da espaçonave 
        self.ship_limit = 3
        # Configurações dos projéteis 
        #self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        #self.ship_speed_factor = 1.5
        self.bullets_allowed = 3

        #configuracao dos alieniginas
        #self.alien_speed_factor = 0.3
        self.fleet_drop_speed = 10

        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        #inicializa configs
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 0.3

        # Scorres
        self.alien_points = 50

        # fleet_direction = 1 =direita; -1 =esquerda 
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)