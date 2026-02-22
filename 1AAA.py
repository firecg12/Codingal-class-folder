import pygame
import random

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Two Sprites with Custom Color Change Event")
# Text settings
font = pygame.font.SysFont(None, 36)
text = font.render("Give me 5 stars Pls. ⭐🌟", True, (255, 255, 255))

# Custom event for changing color
CHANGE_COLOR_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_COLOR_EVENT, 2000)  # Trigger every 2 seconds

# Sprite class
class ColorSprite(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        self.image = pygame.Surface((100, 100))
        self.color = color
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def change_color(self):
        # Generate random color
        self.color = (random.randint(0, 255),
                      random.randint(0, 255),
                      random.randint(0, 255))
        self.image.fill(self.color)

# Create two sprites
sprite1 = ColorSprite((255, 0, 0), 100, 150)
sprite2 = ColorSprite((0, 0, 255), 350, 150)

# Sprite group
all_sprites = pygame.sprite.Group()
all_sprites.add(sprite1, sprite2)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Handle custom color change event
        if event.type == CHANGE_COLOR_EVENT:
            sprite1.change_color()
            sprite2.change_color()

    screen.fill((30, 30, 30))  # Background color
    all_sprites.draw(screen)
    screen.blit(text, (150, 50))  # Draw text
    pygame.display.flip()
    clock.tick(60)

pygame.quit()