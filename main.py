import pygame
from assets.spritesheet import SpriteSheet
from entities.pet import Pet
from ui.components import StatDisplay

# Constants
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
FPS = 60
BG = (50, 50, 50)
BLACK = (0, 0, 0)

# Pygame setup
pygame.init()
pygame.display.set_caption("codeCritters")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# Load sprite sheet
sprite_sheet_image = pygame.image.load('assets/blue_dino.png').convert_alpha()
sprite_sheet = SpriteSheet(sprite_sheet_image)

# Create animation list
animation_list = []
animation_steps = [4, 6, 3, 4]  # Example: idle, walk, kick, hurt
action = 0
frame = 0
last_update = pygame.time.get_ticks()
animation_cooldown = 100
step_counter = 0

for animation in animation_steps:
    temp_list = []
    for _ in range(animation):
        temp_list.append(sprite_sheet.get_image(step_counter, 24, 24, 3, BLACK))
        step_counter += 1
    animation_list.append(temp_list)

# Drag-and-drop setup
sprite_pos = pygame.Vector2(100, 100)
dragging = False
offset_x = 0
offset_y = 0

# create a pet instance
pet = Pet(name="Blue Dino", health=80, hunger=30, energy=70)

# create a stat display
stat_display = StatDisplay(10, 10)
stat_display.initialize()

running = True
while running:
    screen.fill(BG)

    # Animate
    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown:
        frame += 1
        last_update = current_time
        if frame >= len(animation_list[action]):
            frame = 0

    # Get current sprite
    current_sprite = animation_list[action][frame]
    sprite_rect = current_sprite.get_rect(topleft=(sprite_pos.x, sprite_pos.y))
    screen.blit(current_sprite, sprite_pos)

    # draw pet stats using StatDisplay Class
    stat_display.draw(screen, pet)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if sprite_rect.collidepoint(event.pos):
                dragging = True
                mouse_x, mouse_y = event.pos
                offset_x = sprite_pos.x - mouse_x
                offset_y = sprite_pos.y - mouse_y

        elif event.type == pygame.MOUSEBUTTONUP:
            dragging = False

        elif event.type == pygame.MOUSEMOTION and dragging:
            mouse_x, mouse_y = event.pos
            sprite_pos.x = mouse_x + offset_x
            sprite_pos.y = mouse_y + offset_y

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()