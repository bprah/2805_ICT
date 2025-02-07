import pygame
import sys
from old.settings import *

from old.Models.AppModel import AppModel

"""
This controls all of the program and listens to the other controllers for events
"""


class AppController:
    def __init__(self):
        pygame.init()
        #  load the data
        self.model = AppModel()

        #  this controls display module width and height
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

    def run(self):
        state = "menu"
        while 1:
            #  the menu controller linked in AppModel, state tracks which controller to run
            if self.model.state == "menu":
                self.model.menu_view.run(self.screen, self.model.menu_model)
                state = self.model.menu_controller.run(self.screen, self.model.menu_model)

            #elif self.model.state == "play":
                #self.model.play_view.run(self.screen, self.model.play_model)
                #self.mode.play_controller.run()

            elif self.model.state == "config":
                print("config")
                self.model.config_view.run(self.screen, self.model.config_model)
                state = self.model.config_controller.run(self.screen, self.model.config_model)

            if state == "menu":
                self.model.state = "menu"

            elif state == "config":
                self.model.state = "config"

            elif state == "exit":
                sys.exit()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("quit")
                    sys.exit()

                pygame.display.flip()
                self.model.clock.tick(60)
