import pygame
from spritesheet import SpriteSheet

SCREEN_HEIGHT = 480
SCREEN_WIDTH = 640
FPS = 60
FRAMES = FPS / 6
BG = (50, 50, 50)
BLACK = (0, 0, 0)


# pygame setup
pygame.init()
pygame.display.set_caption("codeCritters")
screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
clock = pygame.time.Clock()

#sprite loading
sprite_sheet_image = pygame.image.load('assets/blue_dino.png').convert_alpha()
sprite_sheet = SpriteSheet(sprite_sheet_image)


#create animation list
animation_list = []
animation_steps = [4, 6, 3, 4]
action = 0
last_update = pygame.time.get_ticks()
animation_cooldown = 100
frame = 0
step_counter = 0

for animation in animation_steps:
    temp_img_list = []
    for _ in range(animation):
        temp_img_list.append(sprite_sheet.get_image(step_counter, 24, 24, 3, BLACK))
        step_counter += 1
    animation_list.append(temp_img_list)

running = True

while running:

    #update background
    screen.fill(BG)

    #update animation
    current_time = pygame.time.get_ticks()
    if current_time - last_update >=animation_cooldown:
        frame += 1
        last_update = current_time
        if frame>= len(animation_list[action]):
            frame = 0

    #show frame image
    screen.blit(animation_list[action][frame], (0,0))
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    pygame.display.update()

    clock.tick(60)  # limits FPS to 60

pygame.quit()