
import pygame

pygame.init()
window = pygame.display.set_mode((400, 400))

window.fill((255, 255, 255))

Red = (255, 0, 0)

Blue = (0, 0, 255)

Black = (0, 0, 0)

Green = (0, 255, 0)
Circle1 =  pygame.draw.circle(window, Green, (100, 100), 50), pygame.draw.circle(window, Black, (100, 100), 50, 3)
Circle2 = pygame.draw.circle(window, Blue, (200, 200), 50), pygame.draw.circle(window, Red, (200, 200), 50, 10)





pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()