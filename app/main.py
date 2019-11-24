import board as brd
import random as rnd

print("Let's start here")


def mainGame():
    newboard = brd.Board()
    newboard.create()
    vstee = 0
    # todo: random player selection
    vplayer = 1
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
        vplayer = vplayer*(-1)
        vstee += 1


def smartmoves(isinit, board, player):
    if isinit == 1:
        # vxp = rnd.randint(0,2)
        # vyp = rnd.randint(0,2)
        # board[vxp][vyp] = player
        board[0][2] = player
    else:
        opponent = -1*player
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
# TODO: Diagonal blocks to be done
    return board

mainGame()