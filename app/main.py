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
            print(newboard.showFlat())
            print(newboard.show())
        else:
            newboard = smartmoves(isinit = 0, board = newboard, player = vplayer)
            print(newboard.showFlat())
            print(newboard.show())
        vplayer = vplayer*(-1)
        vstee += 1


def smartmoves(isinit, board, player):
    if isinit == 1:
        # vxp = rnd.randint(0,2)
        # vyp = rnd.randint(0,2)
        # board[vxp][vyp] = player
        board[0][1] = player
    else:
        opponent = -1*player
        print(opponent)
        print(board[0][1])
        if (board[0][1] == opponent or 
            board[2][1] == opponent or
            board[1][0] == opponent or
            board[1][2] == opponent):
            board[1][1] = player
    return board

mainGame()