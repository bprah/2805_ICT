from abc import ABC, abstractmethod


class Factory(ABC):
    """
    An abstract class representing the factory
    """

    @abstractmethod
    def make_enemy(self, window, position, index: int):
        """
        Creates an enemy
        """


class GhostFactory(Factory):
    """
    Factory that creates Ghosts
    """

    def make_enemy(self, window, position, index: int) -> Enemy:
        """
        Produces a ghost based on its index

        :param window: The game window
        :param position: The starting position of the Ghost
        :param index: Number assigned to the ghost
        :return: A instance of a Ghost depending on the index provided.
        """
        if index == "1":
            return RedGhost(window, position, index)
        if index == "2":
            return CyanGhost(window, position, index)
        if index == "3":
            return PinkGhost(window, position, index)
        if index == "4":
            return OrangeGhost(window, position, index)
        return None


class Enemy:
    """
    Handles the enemy movement and display within the game
    """

    def __init__(self, window, position, index: int) -> None:
        """
        Initialises the enemy
        :param window: The game window
        :param position: The starting position of the enemy
        :param index: Number assigned to the Enemy
        """
        self.window = window
        self.grid_position = position
        self.pixel_position = self.get_pixel_position()
        self.radius = self.window.grid_width // 2.3
        self.number = index

        # Upon creation no movement
        self.direction = vec(0, 1)

        self.target = None

    def get_pixel_position(self):
        """
        Returns the pixel position of the Ghost
        :return: Vector tuple: (X_position , Y_position)
        """
        return vec((self.grid_position.x * self.window.grid_width + self.window.grid_width // 2),
                   (self.grid_position.y * self.window.grid_height + self.window.grid_height // 2))

    def update(self):
        """
        Updates whether the enemy can move as well as the grid position based on pixel position
        """
        self.pixel_position += self.direction
        if self.can_move():
            self.move()

        self.grid_position.x = self.pixel_position.x // self.window.grid_width
        self.grid_position.y = self.pixel_position.y // self.window.grid_height

    def can_move(self):
        """
        Checks that the enemy is within the bounds of the maze then checks if their movement is positive.

        :return: True : if able to move
                 False: if not able to move.
        """
        # Checks the X direction to make sure enemy is within the maze then checks that the enemy is moving along the
        # X direction
        if (self.pixel_position.x + self.window.grid_width // 2) % self.window.grid_width == 0:
            if self.direction == vec(1, 0) or self.direction == vec(-1, 0):
                return True
        # Same as above just for the Y Plane
        if (self.pixel_position.y + self.window.grid_height // 2) % self.window.grid_height == 0:
            if self.direction == vec(0, 1) or self.direction == vec(0, -1):
                return True
        return False

    def move(self):
        """
        Sets the movement type of the Enemy based on personality

        """
        if self.personality == 'random':
            self.direction = self.get_random_direction()
        if self.personality == 'seek':
            self.direction = self.get_path_direction()

    def get_path_direction(self):
        """

        :return: A vector as a tuple containing the x & y direction eg (x_direction, y_direction)
        """
        next_cell = self.find_next_cell()
        x_direction = next_cell[0] - self.grid_position[0]
        y_direction = next_cell[1] - self.grid_position[1]
        return vec(x_direction, y_direction)

    def find_next_cell(self):
        """
        Determines the next cell to move to get to the player
        :return:
        """
        path = self.BFS([int(self.grid_position.x), int(self.grid_position.y)], [
            int(self.window.player.grid_position.x), int(self.window.player.grid_position.y)])
        return path[1]

    def BFS(self, start, target):
        """
        When called returns a list with the shortest path to the player based on a Breadth First Search
        :param start: This is the start position of the enemy in a list containing the X&Y co-ordinates as integers
                eg [1,1]
        :param target: This is the current position of the player in a list containing the X&Y co-ordinates as integers
                eg [1,1]
        :return: A list containing cells in list format (list within a list) which when followed will give the shortest
                path to the player. Eg [[x1,y1],[x2,y2],etc]
        """
        # Creation of grid based on maze
        grid = [[0 for x in range(30)] for x in range(30)]
        for cell in self.window.walls:
            if cell.x < 30 and cell.y < 30:
                grid[int(cell.y)][int(cell.x)] = 1

        queue = [start]
        path = []
        visited = []
        while queue:
            current = queue[0]
            queue.remove(queue[0])
            visited.append(current)
            if current == target:
                break
            else:
                neighbours = [[0, -1], [1, 0], [0, 1], [-1, 0]]
                for neighbour in neighbours:
                    if neighbour[0] + current[0] >= 0 and neighbour[0] + current[0] < len(grid[0]):
                        if neighbour[1] + current[1] >= 0 and neighbour[1] + current[1] < len(grid):
                            next_cell = [neighbour[0] + current[0], neighbour[1] + current[1]]
                            if next_cell not in visited:
                                if grid[next_cell[1]][next_cell[0]] != 1:
                                    queue.append(next_cell)
                                    path.append({"Current": current, "Next": next_cell})
        shortest = [target]
        while target != start:
            for step in path:
                if step["Next"] == target:
                    target = step["Current"]
                    shortest.insert(0, step["Current"])
        return shortest

    def get_random_direction(self):
        """
        Gives a random direction to the enemy when called
        :return: A Vector as a  Tuple: (x_direction, y_direction)
        """
        while True:
            number = random.randint(-2, 1)
            if number == -2:
                x_direction, y_direction = 1, 0
            elif number == -1:
                x_direction, y_direction = 0, 1
            elif number == 0:
                x_direction, y_direction = -1, 0
            else:
                x_direction, y_direction = 0, -1
            next_position = vec(self.grid_position.x + x_direction, self.grid_position.y + y_direction)
            if next_position not in self.window.walls:
                break
        return vec(x_direction, y_direction)

    def draw(self):
        """
        Displays the enemy in the game window when called based on color, position and radius.
        :return:
        """
        pygame.draw.circle(self.window.screen, self.colour, (self.pixel_position.x, self.pixel_position.y), self.radius)


class RedGhost(Enemy):
    """
    Representation of the Red Ghost with appropriate color and personality
    """

    def __init__(self, window, position, index):
        super().__init__(window, position, index)
        self.colour = RED = (255, 0, 0)
        self.personality = "seek"


class PinkGhost(Enemy):
    """
    Representation of the Pink Ghost with appropriate color and personality
    """

    def __init__(self, window, position, index):
        super().__init__(window, position, index)
        self.colour = BRILLIANT_LAVENDER = (255, 184, 255)
        self.personality = "pursue"


class CyanGhost(Enemy):
    """
    Representation of the Cyan Ghost with appropriate color and personality

    """

    def __init__(self, window, position, index):
        super().__init__(window, position, index)
        self.colour = AQUA = (0, 255, 255)
        self.personality = "random"


class OrangeGhost(Enemy):
    """
    Representation of the Orange Ghost with appropriate color and personality

    """

    def __init__(self, window, position, index):
        super().__init__(window, position, index)
        self.colour = ORANGE = (255, 184, 82)
        self.personality = "opposite"
