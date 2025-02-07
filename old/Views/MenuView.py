from old.settings import *
import pygame

"""
Defines the displayed elements of the menu page
"""


class MenuView():
    def __init__(self):
        self.font = pygame.font.SysFont("arial", 15)
        self.group_members = self.font.render("Blake Jones, Jeremy McGahey, Petar Vidakovic, Brandon Prahaladh", True, WHITE)
        self.class_name = self.font.render("2805ICT - System and Sofware Design", True, WHITE)
        pygame.display.set_caption("Pac-man")
        self.logo = pygame.image.load("assets/logo.bmp")

    def run(self, screen, model):
        screen.fill(BLACK)

        # image var, (left, top)
        screen.blit(self.logo, ((WIDTH - self.logo.get_width()) // 2, 100))
        screen.blit(self.group_members, ((WIDTH - self.group_members.get_width()) // 2, 50))
        screen.blit(self.class_name, ((WIDTH - self.class_name.get_width()) // 2, 20))



