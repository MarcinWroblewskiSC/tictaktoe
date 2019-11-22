class Board():
    def __init__(self):
        self.matrix = [['-' for var_x in range(3)] for var_y in range(3)]
    
    def show(self):
        """ Printing board list as picture"""
        rez = ""
        for cell in self.matrix:
            rez += str(cell) + "\n"
        return rez

    def board_cls(self):
        """Method to clear current board"""
        self.matrix = None
        self.matrix = [['-' for var_x in range(3)] for var_y in range(3)]