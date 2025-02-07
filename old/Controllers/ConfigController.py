from old.Components.button import *
from old.settings import *

"""
Defines functions of config menu
"""


class ConfigController:
    def run(self, screen, model):
        if button(screen, model.font, "Random map", 218.5, 400, 125, 25, lightgrey, slategrey, "random") == "random":
            return "random"
        if button(screen, model.font, "menu", 218.5, 430, 125, 25, lightgrey, slategrey, "menu") == "menu":
            return "menu"
        if button(screen, model.font, "Exit", 218.5, 460, 125, 25, lightgrey, slategrey, "exit") == "exit":
            return "exit"
