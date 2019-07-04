import pygame

class Ship():
    def __init__(self,ai_settings, screen):
        
        # initiating
        self.screen = screen
        self.ai_settings = ai_settings
        
        # loading image
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # setting ship at the position
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)
        
        # moving flages
        self.moving_right = False
        self.moving_left = False
        
        
        
    

    def update(self):
        # updating position
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.moving_speed
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.moving_speed

        # update rect-object based on self.center
        self.rect.centerx = self.center



    def blitme(self):

        # drawing ship at certain location
        self.screen.blit(self.image, self.rect)

