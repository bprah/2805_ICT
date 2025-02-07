from old.Components.button import *
from old.settings import *

"""
Defines the functions of the Menu
"""


class MenuController:
    def run(self, screen, model):
        if button(screen, model.font, "Start", 218.5, 400, 125, 25, lightgrey, slategrey, "play") == "play":
            return "play"
        if button(screen, model.font, "Config", 218.5, 430, 125, 25, lightgrey, slategrey, "config") == "config":
            return "config"
        if button(screen, model.font, "Exit", 218.5, 460, 125, 25, lightgrey, slategrey, "exit") == "exit":
            return "exit"
