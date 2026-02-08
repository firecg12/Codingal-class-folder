import pygame

pygame.init()

# Set up the display
screen = pygame.display.set_mode((1000, 800))

# Main game loop
done = False

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    

    pygame.display.flip()
