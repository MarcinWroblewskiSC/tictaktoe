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

    def clearBoard(self):
        """Method to clear current board"""
        self.matrix = None
        self.matrix = [[0 for var_x in range(3)] for var_y in range(3)]

    def checkWinner(self):
        winner = 0
        if (
            (sum(self.matrix[0]) == 3) or
            (sum(self.matrix[1]) == 3) or
            (sum(self.matrix[2]) == 3) or
            (sum(row[0] for row in self.matrix) == 3) or
            (sum(row[1] for row in self.matrix) == 3) or
            (sum(row[2] for row in self.matrix) == 3) or
            (self.matrix[0][0] + self.matrix[1][1] + self.matrix[2][2] == 3) or
            (self.matrix[0][2] + self.matrix[1][1] + self.matrix[2][0] == 3)
        ): winner = 1
        elif (
            (sum(self.matrix[0]) == -3) or
            (sum(self.matrix[1]) == -3) or
            (sum(self.matrix[2]) == -3) or
            (sum(row[0] for row in self.matrix) == -3) or
            (sum(row[1] for row in self.matrix) == -3) or
            (sum(row[2] for row in self.matrix) == -3) or
            (self.matrix[0][0] + self.matrix[1][1] + self.matrix[2][2] == -3) or
            (self.matrix[0][2] + self.matrix[1][1] + self.matrix[2][0] == -3)
        ): winner = -1
        return winner
