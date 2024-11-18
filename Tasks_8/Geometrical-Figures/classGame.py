import pygame, classBaloon
pygame.init()


class Game():
    def __init__(self):
        self.font = pygame.font.SysFont('DOCKER THREE', 40)

        self.count = 0
        self.FPS = 30
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font('freesansbold.ttf', 18)
        self.score = self.font.render(f'Score : {self.count}', True, (255, 255, 255))
        self.over = False
        self.display = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
        self.background = pygame.image.load('backgroundsky.jpg')
        self.display.blit(self.score, (100, 100))
        self.group = pygame.sprite.LayeredUpdates()
        self.speed = 7

    def update(self):

        self.clock.tick(self.FPS)
        self.display.blit(self.background, (0, 0))
        self.display.blit(self.score, (30, 30))
        self.group.draw(self.display)
        self.group.update()
        for e in self.group:
            if e.rect.y < -2520:
                e.kill()

        pygame.display.update()

    def spawnbaloon(self):
        self.baloon = classBaloon.Baloon(self.speed)
        self.group.add(self.baloon)
        self.update()

    def checkclick(self, pos):
        sprtlist = self.group.get_sprites_at(pos)
        for k in sprtlist:
            k.kill()
            self.count+=1
            self.score = self.font.render(f'Score : {self.count}', True, (255, 255, 255))
            pygame.mixer.Sound.play(self.baloon.popping_sound)
        self.update()

    def speedup(self):
        self.speed += 2

