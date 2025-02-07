import pygame
from old.settings import *

def text_object(text, font):
    """

    :param text:
    :param font:
    :return:
    """
    text_surface = font.render(text, True, blackish)
    return text_surface, text_surface.get_rect()


def button(screen, font, label, x, y, w, h, hover_color, default_color, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, hover_color, (x, y, w, h))
        if click[0] == 1 and action is not None:
            return action
    else:
        pygame.draw.rect(screen, default_color, (x, y, w, h))

    text_surf = font.render(label, True, blackish)
    text_rect = text_surf.get_rect()

    text_rect.center = ((x + (w // 2)), (y + (h // 2)))
    screen.blit(text_surf, text_rect)
