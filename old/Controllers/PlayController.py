import pygame

"""

"""
class PlayController:
    def __init__(self, model):
        self.load_images(model)

    def run(self):
        pass

    def load_images(self, model):
        """
        Loads images for the maze and also loads the maze text file for displaying enemies, player and wall locations.
        :return:
        """
        model.maze = pygame.image.load("Assets/black_back.bmp")
        # self.maze = pygame.transform.scale(self.maze, (WIDTH, MAZE_HEIGHT))
        # Opening the maze file and making a list fo the walls within
        with open("Views/maze", 'r') as file:
            for y_index, line in enumerate(file):
                for x_index, char in enumerate(line):
                    if char == "1":
                        model.walls.append(model.vectors(x_index, y_index))
                    elif char in ["2", "3", "4", "5"]:
                        model.enemy_position.append(model.vectors(x_index, y_index))
                    elif char == "C":
                        model.coins.append(model.vectors(x_index, y_index))
                    elif char == 'P':
                        model.player_position = [x_index, y_index]
                    elif char == "X":
                        model.power_pellets.append(model.vectors(x_index, y_index))
