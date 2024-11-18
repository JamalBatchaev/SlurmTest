import pygame
from random import choice, randint
pygame.init()

listimage = [pygame.image.load('balloon_blue.png'), pygame.image.load('balloon_red.png'), pygame.image.load('balloon_green.png')]
popping_sound=pygame.mixer.Sound('popping_sound.wav')

class Baloon(pygame.sprite.Sprite):
    def __init__(self, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = choice(listimage)
        self.rect = self.image.get_rect()
        self.rect.x = randint(0, 1720)
        self.rect.y = randint(980, 1280)
        self.speed = speed
        self.popping_sound=popping_sound


    def up(self):
        self.rect.y -= self.speed

    def update(self):
        self.up()
