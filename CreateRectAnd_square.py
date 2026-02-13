import pygame

pygame.init()

# Window setup
WIDTH, HEIGHT = 900, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rectangle Visual Demo")

# Colors
RED = (255, 0, 0)
BLUE = (0, 125, 255)
WHITE = (255, 255, 255)

# Font
font = pygame.font.Font(None, 36)

# Clock & loop control
clock = pygame.time.Clock()
done = False

# Rectangle setup
rect = pygame.Rect(450, 400, 70, 50)
speed = 3  # pixels per frame

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Check keys held down
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        rect.y -= speed
    if keys[pygame.K_DOWN]:
        rect.y += speed
    if keys[pygame.K_LEFT]:
        rect.x -= speed
    if keys[pygame.K_RIGHT]:
        rect.x += speed

    # Clear screen
    screen.fill(WHITE)

    # Draw rectangle
    pygame.draw.rect(screen, BLUE, rect)

    # Draw text
    text = font.render("This is a rectangle ⬇️", True, RED)
    screen.blit(text, (450, 350))

    # Update display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
