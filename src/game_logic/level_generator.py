from random import Random


class LevelGenerator:
    """Class for constructing a simple grid as a blueprint for the minefield

    Attributes:
        random: a Random-object for random number generation
        level: the grid that is being constructed
        width: widht of the grid
        height: height of the grid
        mines: total mine count of the grid
    """

    def __init__(self):
        """Constructor which creates a random number generator needed for the level generation
        """
        self.random = Random()
        self.level = []
        self.width = 0
        self.height = 0
        self.mines = 0

    def generate_level(self, width, height, mines):
        """Generates a level with the chosen parameters

        Args:
            width: width of the grid
            height: height of the grid
            mines: total minecount of the grid

        Returns:
            self.level: 2D array that displays the values of each cell in the grid
        """
        self.level = []
        self.width = width
        self.height = height
        self.mines = mines

        self._generate_grid()
        self._generate_mines()

        return self.level

    def _generate_grid(self):
        """Generates an empty grid with width and height based on the given parameters
        """
        for _ in range(self.height):
            row = []
            for _ in range(self.width):
                row.append(0)
            self.level.append(row)

    def _generate_mines(self):
        """Inserts mines into a random blank positions in the grid until they've all been placed
        """
        for _ in range(self.mines):
            test = -1
            while test == -1:
                x = self.random.randrange(self.width)
                y = self.random.randrange(self.height)
                test = self.level[y][x]
            self._add_mine(x, y)

    def _add_mine(self, x, y):
        """Adds a mine into the chosen position
        Appropriately raises the value of each surrounding non-mine tile by one
        """
        self.level[y][x] = -1
        for num_x in range(x-1, x+2):
            for num_y in range(y-1, y+2):
                if num_x < 0 or num_x >= self.width or num_y < 0 or num_y >= self.height:
                    continue
                if self.level[num_y][num_x] > -1:
                    self.level[num_y][num_x] += 1
