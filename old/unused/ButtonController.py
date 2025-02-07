import pygame

"""
Defines the functionality of the button
"""


class ButtonController:
    def run(self, model):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if model.x + model.w > mouse[0] > model.x and model.y + model.h > mouse[1] > model.y:
            model.color = model.hovercolor
            if click[0] == 1 and model.action is not None:
                return model.action
        else:
            model.color = model.defaultcolor
