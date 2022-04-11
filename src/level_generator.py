from random import Random

class LevelGenerator:
    def __init__(self):
        self.random = Random()
        self.level = []
        self.width = 0
        self.height = 0
        self.mines = 0

    def generate_level(self, width, height, mines):
        self.level = []
        self.width = width
        self.height = height
        self.mines = mines

        self._generate_grid()
        self._generate_mines()

        return self.level
    
    def _generate_grid(self):
        for y in range(self.height):
            row = []
            for x in range(self.width):
                row.append(0)
            self.level.append(row)
    
    def _generate_mines(self):
        for m in range(self.mines):
            test = -1
            while test == -1:
                x = self.random.randrange(self.width)
                y = self.random.randrange(self.height)
                # print(str(x) + ", " + str(y))
                test = self.level[y][x]
            self._add_mine(x, y)

    def _add_mine(self, x, y):
        self.level[y][x] = -1
        for numX in range(x-1, x+2):
            for numY in range(y-1, y+2):
                if numX > -1 and numX < self.width and numY > -1 and numY < self.height:
                    if self.level[numY][numX] > -1:
                        self.level[numY][numX] += 1