class Board():
    def __init__(self):
        self.matrix = []

    def create(self):
        self.matrix = [[0 for var_x in range(3)] for var_y in range(3)]
        return self.matrix

    def __getitem__(self, keyx):
        return self.matrix[keyx]

    def show(self):
        """ Printing board list as picture"""
        rez = ""
        for cell in self.matrix:
            rez += str(cell) + "\n"
        return rez

    def showFlat(self):
        rez = self.matrix
        return rez

    def board_cls(self):
        """Method to clear current board"""
        self.matrix = None
        self.matrix = [[0 for var_x in range(3)] for var_y in range(3)]