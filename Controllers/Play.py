from Models.Player import *
from Models.Enemy import *
from Views.Settings import *
import time

import sys
import pygame

# Initialisation of Pygame
pygame.init()
# For later use in handling movement.
vectors = pygame.math.Vector2

PLAYER_START_POS = vectors(1, 1)

font_score = pygame.font.SysFont("arial", 25)


class Play:
    """
    A class for handling the game window and state
    """

    def __init__(self):
        """

        """
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
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
        self.load_images()
        self.grid_width = (WIDTH // COLS)
        self.grid_height = (MAZE_HEIGHT // ROWS)
        self.player = Player(self, self.player_position)
        self.make_enemies()

    def load_images(self):
        """
        Loads images for the maze and also loads the maze text file for displaying enemies, player and wall locations.
        :return:
        """
        self.maze = pygame.image.load("Assets/black_back.bmp")
        # self.maze = pygame.transform.scale(self.maze, (WIDTH, MAZE_HEIGHT))
        # Opening the maze file and making a list fo the walls within
        with open("Views/maze", 'r') as file:
            for y_index, line in enumerate(file):
                for x_index, char in enumerate(line):
                    if char == "1":
                        self.walls.append(vectors(x_index, y_index))
                    elif char in ["2", "3", "4", "5"]:
                        self.enemy_position.append(vectors(x_index, y_index))
                    elif char == "C":
                        self.coins.append(vectors(x_index, y_index))
                    elif char == 'P':
                        self.player_position = [x_index, y_index]
                    elif char == "X":
                        self.power_pellets.append(vectors(x_index, y_index))

    def make_enemies(self):
        """
        Creates enemies based on
        :return:
        """
        for index, position in enumerate(self.enemy_position):
            self.enemies.append(Enemy(self, position, index))

    def draw_grid(self):
        """
        Function for displaying a grid on the screen
        """
        # Vertical Grid Lines
        # for x in range(WIDTH // self.grid_width):
        #    pygame.draw.line(self.maze, (WHITE), (x * self.grid_width, 0), (x * self.grid_width, HEIGHT))
        # # Horizontal Grid Lines
        # for x in range(HEIGHT // self.grid_height):
        #    pygame.draw.line(self.maze, (WHITE), (0, x * self.grid_height), (WIDTH, x * self.grid_height))
        # Display of walls - should be commented out after testing.
        for wall in self.walls:
            pygame.draw.rect(self.maze, BLUE, (wall.x * self.grid_width, wall.y * self.grid_height,
                                               self.grid_width, self.grid_height))

        # for coin in self.coins:
        #    pygame.draw.rect(self.maze,(167,179,35),(coin.x * self.grid_width, coin.y * self.grid_height,
        #                                        self.grid_width, self.grid_height))

    def run(self):
        """
        Function to run the main game loop while the game is active

        """
        while self.game_active:
            if self.game_state == 'running':
                self.events()
                self.update()
                self.draw()
            elif self.game_state == 'game over':
                self.game_over_events()
                self.game_over_update()
                self.game_over_draw()
            elif self.game_state == 'you win':
                self.game_over_events()
                self.game_over_update()
                self.game_win_draw()

            self.clock.tick(FPS)

        # The window terminates after the loop ends
        pygame.quit()
        sys.exit()

    def draw_text(self, words, screen, pos, size, colour, font_name, centered=False):
        """
        :param words:
        :param screen:
        :param pos:
        :param size:
        :param colour:
        :param font_name:
        :param centered:
        """
        font = pygame.font.SysFont(font_name, size)
        text = font.render(words, False, colour)
        text_size = text.get_size()
        if centered:
            pos[0] = pos[0] - text_size[0] // 2
            pos[1] = pos[1] - text_size[1] // 2
        screen.blit(text, pos)

    def events(self):
        """
        Handling of events that are happening within the game window. Key presses control player movement and closing
        of the window closes the game.


        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_active = False
            if event.type == pygame.USEREVENT:
                self.power_pellet_active = False
                for enemy in self.enemies:
                    enemy.set_personality()
                    enemy.set_colour()
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    self.player.move(vec(-1, 0))

                if event.key == pygame.K_RIGHT:
                    self.player.move(vec(1, 0))

                if event.key == pygame.K_UP:
                    self.player.move(vec(0, -1))
                if event.key == pygame.K_DOWN:
                    self.player.move(vec(0, 1))

    def update(self):
        """
        Calls the update command for objects within the game to ensure correct functioning

        """
        self.player.update()
        for enemy in self.enemies:
            enemy.update()

        for enemy in self.enemies:
             if enemy.grid_position == self.player.grid_position:
                if self.power_pellet_active:
                    self.player.current_score += 100
                    enemy.grid_position = vec(enemy.starting_pos)
                    enemy.pixel_position = enemy.get_pixel_position()
                    enemy.direction *= 0
                    enemy.personality = enemy.set_personality()
                    enemy.colour = enemy.set_colour()
                else:
                    self.remove_life()

        if self.player.current_score == 2870:
            self.game_state = 'you win'

        if self.player.on_power_pellet():
            self.player.eat_power_pellet()
            self.power_pellet_active = True
            self.power_pellet_timer = time.time()
            for enemy in self.enemies:
                enemy.personality = 'scared'
                enemy.colour = BLUE
        # When 10 seconds has passed reset enemies
        if time.time() - self.power_pellet_timer > 10:
            for enemy in self.enemies:
                enemy.personality = enemy.set_personality()
                enemy.colour = enemy.set_colour()
                self.power_pellet_active = False




    def draw(self):
        """
        Function for refreshing the display

        """
        score_text = font_score.render("Score:{}".format(self.player.current_score), True, WHITE)

        self.screen.blit(self.maze, (0, 0))
        self.draw_coins()
        # self.draw_text("Score: 0", self.screen, [60,0], 18, WHITE, START_FONT)
        self.draw_power_pellets()
        self.draw_grid()
        self.player.draw()
        self.screen.blit(score_text, (5, 630))

        for enemy in self.enemies:
            enemy.draw()

        pygame.display.update()

    def reset(self):
        self.player.lives = 3
        self.player.current_score = 0
        self.player.grid_position = vec(self.player.starting_pos)
        self.player.pixel_position = self.player.get_pix_pos()
        self.player.direction *= 0
        for enemy in self.enemies:
            enemy.grid_position = vec(enemy.starting_pos)
            enemy.pixel_position = enemy.get_pixel_position()
            enemy.direction *= 0
        self.coins = []
        with open("../Views/maze", 'r') as file:
            for y_index, line in enumerate(file):
                for x_index, char in enumerate(line):
                    if char == "C":
                        self.coins.append(vectors(x_index, y_index))


    def remove_life(self):
        if self.power_pellet_active:
            return
        else:
            self.player.lives -= 1
            if self.player.lives == 0:
                self.game_state = 'game over'
            else:
                self.player.grid_position = vectors(self.player.starting_pos)
                self.player.pixel_position = self.player.get_pix_pos()
                self.player.direction *= 0
                for enemy in self.enemies:
                    enemy.grid_position = vec(enemy.starting_pos)
                    enemy.pixel_position = enemy.get_pixel_position()
                    enemy.direction *= 0


    def draw_coins(self):
        """
        Displays a circle on the screen to represent the coins

        """
        for coin in self.coins:
            pygame.draw.circle(self.screen, WHITE,
                               (int(coin.x * self.grid_width) + self.grid_width // 2,
                                int(coin.y * self.grid_height) + self.grid_height // 2), 4)
    def draw_power_pellets(self):
        """
        Displays a circle on the screen to represent the coins

        """
        for coin in self.power_pellets:
            pygame.draw.circle(self.screen, WHITE,
                               (int(coin.x * self.grid_width) + self.grid_width // 2,
                                int(coin.y * self.grid_height) + self.grid_height // 2), 8)

##########################      GAME OVER EVENTS        ########################


    def game_over_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_active = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.reset()
                self.game_state = 'running'
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.game_active = False

    def game_over_update(self):
        pass

    def game_win_draw(self):
        self.screen.fill(BLACK)
        self.draw_text("You Win!!!!", self.screen, [WIDTH // 2, HEIGHT // 3], 36, WHITE, START_FONT, centered=True)
        self.draw_text("Press Space to play again", self.screen, [WIDTH // 2, HEIGHT // 2], 20, WHITE, START_FONT, centered=True)
        self.draw_text("Press Escape to Quit", self.screen, [WIDTH // 2, HEIGHT // 1.7], 20, WHITE, START_FONT, centered=True)
        pygame.display.update()


    def game_over_draw(self):
        self.screen.fill(BLACK)
        self.draw_text("Game Over", self.screen, [WIDTH // 2, HEIGHT // 3], 36, WHITE, START_FONT, centered=True)
        self.draw_text("Press Space to play again", self.screen, [WIDTH // 2, HEIGHT // 2], 20, WHITE, START_FONT, centered=True)
        self.draw_text("Press Escape to Quit", self.screen, [WIDTH // 2, HEIGHT // 1.7], 20, WHITE, START_FONT, centered=True)
        pygame.display.update()



