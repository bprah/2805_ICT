from Controllers.Play import *
from Views.Settings import *
from pygame import mixer

mixer.init()
pygame.init()

clock = pygame.time.Clock()

# main font
font = pygame.font.SysFont("arial", 15)

# group stuff
group_members = font.render("Blake Jones, Jeremy McGahey, Petar Vidakovic, Brandon Prahaladh", True, WHITE)
class_name = font.render("2805ICT - System and Sofware Design", True, WHITE)

# game intro sound
intro_sound = pygame.mixer.Sound("sounds/intro_sound.wav")

# screen settings
start_screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pac-man")

# load logo image
logo = pygame.image.load("Assets/logo.bmp")


def text_object(text, font):
    """

    :param text:
    :param font:
    :return:
    """
    text_surface = font.render(text, True, blackish)
    return text_surface, text_surface.get_rect()


def button(msg, x, y, w, h, hovercolor, defaultcolor, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(start_screen, hovercolor, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(start_screen, defaultcolor, (x, y, w, h))

    textSurf, textRect = text_object(msg, font)
    textRect.center = ((x + (w // 2)), (y + (h // 2)))
    start_screen.blit(textSurf, textRect)


# launcd the game to play
def create_play():
    # pygame.mixer.Sound.play(intro_sound)
    play = Play()
    play.run()


# config page
def create_config():
    config_text = font.render("Config menu", True, WHITE)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        start_screen.fill(BLACK)
        start_screen.blit(config_text, ((WIDTH - config_text.get_width()) / 2, 15))

        button("Random map", 218.5, 400, 125, 25, lightgrey, slategrey, create_Rmap)
        button("Menu", 218.5, 430, 125, 25, lightgrey, slategrey, create_menu)
        button("Exit", 218.5, 460, 125, 25, lightgrey, slategrey, create_exit)

        pygame.display.update()
        clock.tick(15)



def create_Rmap():
    pass


def create_exit():
    pygame.quit()
    sys.exit()


# main start page
def create_menu():
    while True:
        start_screen.fill(BLACK)

        # image var, (left, top)
        start_screen.blit(logo, ((WIDTH - logo.get_width()) // 2, 100))
        start_screen.blit(group_members, ((WIDTH - group_members.get_width()) // 2, 50))
        start_screen.blit(class_name, ((WIDTH - class_name.get_width()) // 2, 20))

        button("Start", 218.5, 400, 125, 25, lightgrey, slategrey, create_play)
        button("Config", 218.5, 430, 125, 25, lightgrey, slategrey, create_config)
        button("Exit", 218.5, 460, 125, 25, lightgrey, slategrey, create_exit)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit

        pygame.display.update()
        clock.tick(15)


# game loop
while True:

    create_menu()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(15)
