import pygame
import random
print("please start giving me five stars")
pygame.init()

Sprite_Color_Change_Event = pygame.USEREVENT + 1
Background_Color_Change_Event = pygame.USEREVENT + 2

Blue = pygame.Color('blue')
Light_Blue = pygame.Color('lightblue')
Dark_Blue = pygame.Color('darkblue')
Red = pygame.Color('red')
Yellow = pygame.Color('yellow')
Orange = pygame.Color('orange')
White = pygame.Color('white')

COLOR_LIST = [Blue, Light_Blue, Dark_Blue, Red, Yellow, Orange, White]


class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

        # Fixed velocity (no constant -1)
        self.velocity = [
            random.choice([-1, 1]),
            random.choice([-1, 1])
        ]

    def update(self):
        self.rect.move_ip(self.velocity)

        boundary_hit = False

        if self.rect.left <= 0 or self.rect.right >= 500:
            self.velocity[0] = -self.velocity[0]
            boundary_hit = True

        if self.rect.top <= 0 or self.rect.bottom >= 400:
            self.velocity[1] = -self.velocity[1]
            boundary_hit = True

        if boundary_hit:
            pygame.event.post(pygame.event.Event(Sprite_Color_Change_Event))
            pygame.event.post(pygame.event.Event(Background_Color_Change_Event))

    def change_color(self, color):
        self.image.fill(color)


all_sprites = pygame.sprite.Group()

sp1 = Sprite(White, 20, 30)
sp1.rect.x = random.randint(0, 480)
sp1.rect.y = random.randint(0, 370)

all_sprites.add(sp1)

sp2 = Sprite(Red, 30, 40)
sp2.rect.x = random.randint(0, 470)
sp2.rect.y = random.randint(0, 360)

all_sprites.add(sp2)

screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("BUDR SRT")

background_color = Blue
clock = pygame.time.Clock()

exit = False  # Fixed

while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

        elif event.type == Sprite_Color_Change_Event:
            sp1.change_color(random.choice(COLOR_LIST))

        elif event.type == Background_Color_Change_Event:
            background_color = random.choice(COLOR_LIST)

    all_sprites.update()

    screen.fill(background_color)
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(240)

pygame.quit()

            


          
