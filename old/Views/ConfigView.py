from old.settings import *

class ConfigView:
    def run(self, screen, model):
        config_text = model.font.render("Config menu", True, WHITE)
        screen.fill(BLACK)
        screen.blit(config_text, ((WIDTH - config_text.get_width()) / 2, 15))

