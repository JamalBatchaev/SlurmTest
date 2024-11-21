# shapes.py
import pygame
import random

class Shape:
    def __init__(self, x, y, size, color, shape_type):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.shape_type = shape_type
        self.speed_x = random.choice([-4, -3, -2, -1, 1, 2, 3, 4])
        self.speed_y = random.choice([-4, -3, -2, -1, 1, 2, 3, 4])

    def draw(self, screen):
        if self.shape_type == 'circle':
            pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)
        elif self.shape_type == 'square':
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))
        elif self.shape_type == 'triangle':
            points = [(self.x, self.y - self.size), (self.x - self.size, self.y + self.size), (self.x + self.size, self.y + self.size)]
            pygame.draw.polygon(screen, self.color, points)

    def move(self, width, height):
        self.x += self.speed_x
        self.y += self.speed_y

        # Отскок от стен
        if self.x <= 0 or self.x >= width - self.size:
            self.speed_x *= -1
        if self.y <= 0 or self.y >= height - self.size:
            self.speed_y *= -1

    def is_clicked(self, pos):
        if self.shape_type == 'circle':
            return (pos[0] - self.x) ** 2 + (pos[1] - self.y) ** 2 <= self.size ** 2
        elif self.shape_type == 'square':
            return self.x <= pos[0] <= self.x + self.size and self.y <= pos[1] <= self.y + self.size
        elif self.shape_type == 'triangle':
            return (self.x - self.size <= pos[0] <= self.x + self.size) and (self.y - self.size <= pos[1] <= self.y + self.size)

def create_random_shape(width, height):
    size = 30
    x = random.randint(0 + size, width - size)
    y = random.randint(0 + size, height - size)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    shape_type = random.choice(['circle', 'square', 'triangle'])
    return Shape(x, y, size, color, shape_type)