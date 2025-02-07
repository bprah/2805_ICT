from Controllers.Play import *
from Views.Settings import *
import pygame
from pygame import mixer
mixer.init()

vec = pygame.Vector2
#eat_pellet_sound = pygame.mixer.Sound("sounds/eat_pellet.wav")


class Singleton(type):
    instance = None

    def __call__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.instance


class Player(metaclass=Singleton):
    """
    Represents the player within the game
    """
    def __init__(self, window, position):
        """

        Initialisation of the player

        :param window: The game window
        :param position: The starting position of the player
        """
        self.window = window
        self.starting_pos = position
        self.grid_position = vec(position[0], position[1])
        self.pixel_position = vec((self.grid_position.x * self.window.grid_width // 2 + self.window.grid_width),
                                  (self.grid_position.y * self.window.grid_height // 2 + self.window.grid_height))
        # Initial Direction of player
        self.direction = vec(1, 0)
        self.stored_direction = None
        self.able_to_move = True
        self.speed = 2
        self.current_score = 0
        self.lives = 3

    def draw(self):
        """



        """
        # Display the pacman as a circle.
        pygame.draw.circle(self.window.screen, YELLOW, self.pixel_position, self.window.grid_width - 10)
        # Display the grid position in a red rectangle
        # pygame.draw.rect(self.window.screen, WHITE, (self.grid_position[0] * self.window.grid_width,
        #                                            self.grid_position[1] * self.window.grid_height,
        #                                            self.window.grid_width,
        #                                            self.window.grid_height), 1)
        for x in range(self.lives):
            pygame.draw.circle(self.window.screen, YELLOW, (500 + 25 * x, HEIGHT - 12), 10)



    def update(self):
        """

        :return:
        """
        if self.able_to_move:
            self.pixel_position += self.direction * self.speed

        # Deals with movement of pacman along the grid
        # if all conditions are met will allow the pacman in the x direction
        if self.can_move():
            if self.stored_direction is not None:
                self.direction = self.stored_direction
            self.able_to_move = self.not_blocked()

        # Updating the grid position based on the movement of the player
        self.grid_position.x = self.pixel_position.x // self.window.grid_width
        self.grid_position.y = self.pixel_position.y // self.window.grid_height

        # self.grid_position[0] = (self.pixel_position[0] +
        #                          self.window.grid_width // 2) // self.window.grid_width
        # self.grid_position[1] = (self.pixel_position[1] +
        #                          self.window.grid_height // 2) // self.window.grid_height

        if self.on_coin():
            self.eat_coin()

        
    def on_coin(self):
        """

        :return:
        """
        if self.grid_position in self.window.coins:
            return True
        return False

    def on_power_pellet(self):
        """
        Checks if player is on a power pellet

        :return: True- if player is on a power pellet False- if not on power pellet
        """
        if self.grid_position in self.window.power_pellets:
            return True
        return False

    def eat_power_pellet(self):
        """

        :return:
        """
        self.window.power_pellets.remove(self.grid_position)
        #pygame.mixer.Sound.play(eat_pellet_sound)

        self.current_score += 10

    def eat_coin(self):
        """

        :return:
        """
        self.window.coins.remove(self.grid_position)
        #pygame.mixer.Sound.play(eat_pellet_sound)
        self.current_score += 10

    def move(self, direction):
        """

        :param direction:
        :return:
        """
        self.stored_direction = direction

    def get_pix_pos(self):
        """
        Returns the pixel position of the Player
        :return: Vector tuple: (X_position , Y_position)
        """
        return vec((self.grid_position.x * self.window.grid_width + self.window.grid_width // 2),
                   (self.grid_position.y * self.window.grid_height + self.window.grid_height // 2))

    def can_move(self):
        """

        :return:
        """

        if (self.pixel_position.x + self.window.grid_width // 2) % self.window.grid_width == 0:
            if self.direction == vec(1, 0) or self.direction == vec(-1, 0) or self.direction == vec(0, 0):
                return True

        if (self.pixel_position.y + self.window.grid_height // 2) % self.window.grid_height == 0:
            if self.direction == vec(0, 1) or self.direction == vec(0, -1) or self.direction == vec(0, 0):
                return True

        #return False

    def not_blocked(self):
        """
        Checks to see if the player is trying to move into a wall

        :return: True: if the player is moving into a wall
                 False: if player is not moving into a wall
        """
        for wall in self.window.walls:
            if vec(self.grid_position + self.direction) == wall:
                return False
        return True
