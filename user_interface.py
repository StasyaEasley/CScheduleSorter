import pygame
import button

pygame.init()

SCREEN_HEIGHT = 720
SCREEN_WIDTH = 1280

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Class Recs")

start_image = pygame.image.load("start_button.png").convert_alpha()
exit_image = pygame.image.load("exit_button.png").convert_alpha()
schedule_sprite = pygame.image.load("schedule.png").convert_alpha()

start_button = button.Button(450, 300, start_image, 0.5)
exit_button = button.Button(20, 20, exit_image, 0.1)


run = True
while run:
    screen.fill((150, 212, 242))

    if start_button.draw(screen):
        print("Start")
    if exit_button.draw(screen):
        run = False
    # run = False for exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
pygame.quit()
