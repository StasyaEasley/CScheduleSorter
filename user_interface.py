import pygame
import button

pygame.init()

SCREEN_HEIGHT = 720
SCREEN_WIDTH = 1280

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Class Recs")
timer = pygame.time.Clock()


messages = ["Hello, CS Majors! Welcome to your schedule maker.",
            "My job is to recommend CS classes for the future based on what you have already taken!",
            "Shall we get started?"]

text_font = pygame.font.Font("StayPixelRegular-EaOxl.ttf", 40)
text_font_2 = pygame.font.Font("StayPixelRegular-EaOxl.ttf", 30)
text_font_3 = pygame.font.Font("StayPixelRegular-EaOxl.ttf", 60)

snip = text_font.render("", True, "black")
counter = 0
speed = 3
active_message = 0
message = messages[active_message]
done = False

start_image = pygame.image.load("start_button.png").convert_alpha()
exit_image = pygame.image.load("exit_button.png").convert_alpha()

start_button = button.Button(450, 300, start_image, 0.5)
exit_button = button.Button(20, 20, exit_image, 0.1)


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


"""draw_text(messages, text_font, "black", 220, 150)
    draw_text(message_2, text_font_2, "black", 120, 200)
    draw_text(messages, text_font_3, "black", 360, 260)
    """

run = True
while run:
    screen.fill((150, 212, 242))
    timer.tick(60)
    if counter < speed * len(message):
        counter += 1
    elif counter >= speed * len(message):
        done = True
    if start_button.draw(screen):
        print('Start')
    if exit_button.draw(screen):
        run = False
    # run = False for exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and done and active_message < len(messages):
                active_message += 1
                done = False
                message = messages[active_message]
                counter = 0

    snip = text_font_2.render(message[0:counter // speed], True, "black")
    screen.blit(snip, (120, 200))

    pygame.display.flip()
pygame.quit()
