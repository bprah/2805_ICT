import pygame
from old.settings import *

"""
Defines the way the button will be displayed
"""
class ButtonView:
    def __init__(self):
        self.font = pygame.font.SysFont("arial", 15)

    def text_object(self, text, font):
        text_surface = self.font.render(text, True, blackish)
        return text_surface, text_surface.get_rect()

    def run(self, screen, model):
        pygame.draw.rect(screen, model.color, (model.x, model.y, model.w, model.h))
        textSurf, textRect = self.text_object(model.label, self.font)
        textRect.center = ((model.x + (model.w // 2)), (model.y + (model.h // 2)))
        screen.blit(textSurf, textRect)


