import pygame

pygame.init()
screen = pygame.display.set_mode((900, 800))
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    pygame.draw.rect(screen, (0, 125, 255), pygame.Rect(450, 400, 100, 90))
    pygame.display.flip()