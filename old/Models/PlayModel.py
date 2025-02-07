from old.settings import *
import pygame
"""

"""


class PlayModel:
    def __init__(self):
        self.game_active = True
        self.game_state = 'running'
        self.cell_width = MAZE_WIDTH//COLS
        self.cell_height = MAZE_HEIGHT//ROWS
        self.walls = []
        self.coins = []
        self.enemies = []
        self.enemy_position = []
        self.power_pellets = []
        self.power_pellet_active = False
        self.power_pellet_timer = 0
        self.player_position = None
        self.grid_width = (WIDTH // COLS)
        self.grid_height = (MAZE_HEIGHT // ROWS)
        self.vectors = pygame.math.Vector2
        #self.player = Player(self, self.player_position)
