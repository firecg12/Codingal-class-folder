import pygame
import random


SCREEN_WIDTH, SCREEN_HEIGHT = 500, 400
MOVEMENT_SPEED = 5
FONT_SIZE = 72

pygame.init()

backround_image = pygame.image.load("MyFirstGame_Image.png")

font = pygame.font.SysFont("Arial", FONT_SIZE)

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(pygame.Color('dodgerblue'))
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()

    def move(self, x, y):
        self.rect.x += x
        self.rect.y += y
        self.rect.x = max(0, min(self.rect.x, SCREEN_WIDTH - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, SCREEN_HEIGHT - self.rect.height))

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My First Game")
all_sprites = pygame.sprite.Group()

sprite1 = Sprite(pygame.Color('black'), 20, 30)
sprite1.rect.x, sprite1.rect.y = random.randint(0, SCREEN_WIDTH - sprite1.rect.width), random.randint(0, SCREEN_HEIGHT - sprite1.rect.height)
all_sprites.add(sprite1)

sprite2 = Sprite(pygame.Color('red'), 20, 30)
sprite2.rect.x, sprite2.rect.y = random.randint(0, SCREEN_WIDTH - sprite2.rect.width), random.randint(0, SCREEN_HEIGHT - sprite2.rect.height)
all_sprites.add(sprite2)

clock = pygame.time.Clock()

running, won = True, False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_x):

            running = False
    if not won:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            sprite1.move(-MOVEMENT_SPEED, 0)
        if keys[pygame.K_RIGHT]:
            sprite1.move(MOVEMENT_SPEED, 0)
        if keys[pygame.K_UP]:
            sprite1.move(0, -MOVEMENT_SPEED)
        if keys[pygame.K_DOWN]:
            sprite1.move(0, MOVEMENT_SPEED)

        if sprite1.rect.colliderect(sprite2.rect):
            won = True
    screen.blit(backround_image, (0, 0))
    all_sprites.draw(screen)
    if won:
        text = font.render("You Win!", True, pygame.Color('Purple'))
        screen.blit(text, text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)))
        sprite2.kill()
    
    pygame.display.flip()
    
    clock.tick(90)

pygame.quit()
        
