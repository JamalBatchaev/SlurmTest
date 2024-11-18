import pygame
import random
from shapes import Shape, create_random_shape



def main():
    pygame.init()
    width=pygame.display.Info().current_w 
    height=pygame.display.Info().current_h
    fps = 30
    num_shapes = 20

    screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
    pygame.display.set_caption("Popping figures")
    
    clock = pygame.time.Clock()
    shapes = [create_random_shape(width, height) for _ in range(num_shapes)]
    score = 0
    font = pygame.font.Font(None, 36)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for shape in shapes[:]:
                    if shape.is_clicked(pos):
                        shapes.remove(shape)
                        score += 1
                        break

        screen.fill((255, 255, 255))  # Белый фон
        for shape in shapes:
            shape.move(width, height)
            shape.draw(screen)

        # Отображаем счет
        score_text = font.render(f"Score: {score}", True, (0, 0, 0))
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()
if __name__ == "__main__":
    main()