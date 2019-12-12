import board as brd
import random as rnd

print("Let's start here")

def randPlayer():
    player = 0
    while player == 0:
        player = rnd.randint(-1,1)
    return player


def mainGame():
    newboard = brd.Board()
    newboard.create()
    vstee = 0
    # todo: random player selection
    vplayer = randPlayer()
    while vstee <= 8:
        print(vstee)
        if vstee == 0:
            newboard = smartmoves(isinit = 1, board = newboard, player = vplayer)
            print(newboard.show())
            if newboard.checkWinner() != 0:
                print(newboard.checkWinner())
                print("The winner is player: " + str(newboard.checkWinner()))
                break
        else:
            newboard = smartmoves(isinit = 0, board = newboard, player = vplayer)
            print(newboard.show())
            if newboard.checkWinner() != 0:
                print("The winner is player: " + str(newboard.checkWinner()))
                break
        vplayer = -vplayer
        vstee += 1


def smartmoves(isinit, board, player):
    if isinit == 1:
        vxp = rnd.randint(0,2)
        vyp = rnd.randint(0,2)
        board[vxp][vyp] = player
    else:
        opponent = -player
# Final moves section
        if (board[0][0] == player and board[0][1] == player and board[0][2] == 0):
            board[0][2] = player
        elif (board[0][0] == player and board[0][1] == 0 and board[0][2] == player):
            board[0][1] = player
        elif (board[0][0] == 0 and board[0][1] == player and board[0][2] == player):
            board[0][0] = player
        elif (board[1][0] == player and board[1][1] == player and board[1][2] == 0):
            board[1][2] = player
        elif (board[1][0] == player and board[1][1] == 0 and board[1][2] == player):
            board[1][1] = player
        elif (board[1][0] == 0 and board[1][1] == player and board[1][2] == player):
            board[1][0] = player
        elif (board[2][0] == player and board[2][1] == player and board[2][2] == 0):
            board[2][2] = player
        elif (board[2][0] == player and board[2][1] == 0 and board[2][2] == player):
            board[2][1] = player
        elif (board[2][0] == 0 and board[2][1] == player and board[2][2] == player):
            board[2][0] = player
        elif (board[0][0] == 0 and board[1][0] == player and board[2][0] == player):
            board[0][0] = player
        elif (board[0][0] == player and board[1][0] == 0 and board[2][0] == player):
            board[1][0] = player
        elif (board[0][0] == player and board[1][0] == player and board[2][0] == 0):
            board[2][0] = player
        elif (board[0][1] == 0 and board[1][1] == player and board[2][1] == player):
            board[0][1] = player
        elif (board[0][1] == player and board[1][1] == 0 and board[2][1] == player):
            board[1][1] = player
        elif (board[0][1] == player and board[1][1] == player and board[2][1] == 0):
            board[2][1] = player
        elif (board[0][2] == 0 and board[1][2] == player and board[2][2] == player):
            board[0][2] = player
        elif (board[0][2] == player and board[1][2] == 0 and board[2][2] == player):
            board[1][2] = player
        elif (board[0][2] == player and board[1][2] == player and board[2][2] == 0):
            board[2][2] = player
# diagonal final moves
        elif (board[0][0] == player and board[1][1] == player and board[2][2] == 0):
            board[2][2] = player
        elif (board[0][0] == player and board[1][1] == 0 and board[2][2] == player):
            board[1][1] = player
        elif (board[0][0] == 0 and board[1][1] == player and board[2][2] == player):
            board[0][0] = player
        elif (board[0][2] == player and board[1][1] == player and board[2][0] == 0):
            board[2][0] = player
        elif (board[0][2] == player and board[1][1] == 0 and board[2][0] == player):
            board[1][1] = player
        elif (board[0][2] == 0 and board[1][1] == player and board[2][0] == player):
            board[0][2] = player
# Diagonal blocks
        elif (board[0][0] == opponent and board[1][1] == opponent and board[2][2] == 0):
            board[2][2] = player
        elif (board[1][1] == opponent and board[2][2] == opponent and board[0][0] == 0):
            board[0][0] = player
        elif (board[0][0] == opponent and board[2][2] == opponent and board[1][1] == 0):
            board[1][1] = player
        elif (board[2][0] == opponent and board[0][2] == opponent and board[1][1] == 0):
            board[1][1] = player
        elif (board[1][1] == opponent and board[0][2] == opponent and board[2][0] == 0):
            board[2][0] = player
        elif (board[1][1] == opponent and board[2][0] == opponent and board[0][2] == 0):
            board[0][2] = player
# Horizontal line blocks
        elif (board[0][0] == opponent and board[0][1] == opponent and board[0][2] == 0):
            board[0][2] = player
        elif (board[0][1] == opponent and board[0][2] == opponent and board[0][0] == 0):
            board[0][0] = player
        elif (board[0][0] == opponent and board[0][2] == opponent and board[0][1] == 0):
            board[0][1] = player

        elif (board[1][0] == opponent and board[1][1] == opponent and board[1][2] == 0):
            board[1][2] = player
        elif (board[1][1] == opponent and board[1][2] == opponent and board[1][0] == 0):
            board[1][0] = player
        elif (board[1][0] == opponent and board[1][2] == opponent and board[1][1] == 0):
            board[1][1] = player

        elif (board[2][0] == opponent and board[2][1] == opponent and board[2][2] == 0):
            board[2][2] = player
        elif (board[2][1] == opponent and board[2][2] == opponent and board[2][0] == 0):
            board[2][0] = player
        elif (board[2][0] == opponent and board[2][2] == opponent and board[2][1] == 0):
            board[2][1] = player

# Vertical line blocks
        elif (board[0][0] == opponent and board[2][0] == opponent and board[1][0] == 0):
            board[1][0] = player
        elif (board[0][0] == opponent and board[1][0] == opponent and board[2][0] == 0):
            board[2][0] = player
        elif (board[1][0] == opponent and board[2][0] == opponent and board[0][0] == 0):
            board[0][0] = player

        elif (board[0][1] == opponent and board[2][1] == opponent and board[1][1] == 0):
            board[1][1] = player
        elif (board[0][1] == opponent and board[1][1] == opponent and board[2][1] == 0):
            board[2][1] = player
        elif (board[1][1] == opponent and board[2][1] == opponent and board[0][1] == 0):
            board[0][1] = player

        elif (board[0][2] == opponent and board[2][2] == opponent and board[1][2] == 0):
            board[1][2] = player
        elif (board[0][2] == opponent and board[1][2] == opponent and board[2][2] == 0):
            board[2][2] = player
        elif (board[1][2] == opponent and board[2][2] == opponent and board[0][2] == 0):
            board[0][2] = player

# Blocks
        elif board[0][0] == opponent:
            while True:
                x = rnd.randint(0,1)
                y = rnd.randint(0,1)
                if board[x][y] == 0:
                    board[x][y] = player
                    break
                elif (board[0][1] != 0 and board[1][0] != 0 and board[1][1] != 0):
                    break
        elif board[0][1] == opponent:
            while True:
                x = rnd.randint(0,1)
                y = rnd.randint(0,2)
                if board[x][y] == 0:
                    board[x][y] = player
                    break
                elif (
                    board[0][0] != 0 and board[0][2] != 0 and
                    board[1][0] != 0 and board[1][1] != 0 and board[1][2] != 0
                    ):
                    break
        elif board[0][2] == opponent:
            while True:
                x = rnd.randint(0,1)
                y = rnd.randint(1,2)
                if board[x][y] == 0:
                    board[x][y] = player
                    break
                elif (board[0][1] != 0 and board[1][1] != 0 and board[1][2] != 0):
                    break
        elif board[1][0] == opponent:
            while True:
                x = rnd.randint(0,2)
                y = rnd.randint(0,1)
                if board[x][y] == 0:
                    board[x][y] = player
                    break
                elif (
                    board[0][0] != 0 and board[0][1] != 0 and 
                    board[1][1] != 0 and
                    board[2][0] != 0 and board[2][1] != 0
                    ):
                    break
        elif board[1][2] == opponent:
            while True:
                x = rnd.randint(0,2)
                y = rnd.randint(1,2)
                if board[x][y] == 0:
                    board[x][y] = player
                    break
                elif (
                    board[0][2] != 0 and board[0][1] != 0 and 
                    board[1][1] != 0 and
                    board[2][2] != 0 and board[2][1] != 0
                    ):
                    break
        elif board[1][1] == opponent:
            while True:
                x = rnd.randint(0,2)
                y = rnd.randint(0,2)
                if board[x][y] == 0:
                    board[x][y] = player
                    break
                elif (
                    board[0][0] != 0 and board[0][1] != 0 and board[0][2] != 0 and 
                    board[1][0] != 0 and board[1][2] != 0 and
                    board[2][0] != 0 and board[2][1] != 0 and board[2][2] != 0
                    ):
                    break
        elif board[2][0] == opponent:
            while True:
                x = rnd.randint(1,2)
                y = rnd.randint(0,1)
                if board[x][y] == 0:
                    board[x][y] = player
                    break
                elif (board[2][1] != 0 and board[1][0] != 0 and board[1][1] != 0):
                    break
        elif board[2][1] == opponent:
            while True:
                x = rnd.randint(1,2)
                y = rnd.randint(0,2)
                if board[x][y] == 0:
                    board[x][y] = player
                    break
                elif (
                    board[2][0] != 0 and board[2][2] != 0 and
                    board[1][0] != 0 and board[1][1] != 0 and board[1][2] != 0
                    ):
                    break
        elif board[2][2] == opponent:
            while True:
                x = rnd.randint(1,2)
                y = rnd.randint(1,2)
                if board[x][y] == 0:
                    board[x][y] = player
                    break
                elif (board[2][1] != 0 and board[1][1] != 0 and board[1][2] != 0):
                    break
    return board


if __name__ == "__main__":
    mainGame()