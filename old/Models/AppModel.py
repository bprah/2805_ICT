import pygame
from old.Models.MenuModel import MenuModel
from old.Views.MenuView import MenuView
from old.Controllers.MenuController import MenuController

from old.Models.PlayModel import PlayModel
from old.Views.PlayView import PlayView
from old.Controllers.PlayController import PlayController

from old.Models.ConfigModel import ConfigModel
from old.Views.ConfigView import ConfigView
from old.Controllers.ConfigController import ConfigController

"""
This stores the state of the AppController
"""


class AppModel:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.state = "menu"

        self.menu_model = MenuModel()
        self.menu_view = MenuView()
        self.menu_controller = MenuController()

        self.config_model = ConfigModel()
        self.config_view = ConfigView()
        self.config_controller = ConfigController()

        self.play_model = PlayModel()
        self.play_view = PlayView()
        self.play_controller = PlayController(self.play_model)
