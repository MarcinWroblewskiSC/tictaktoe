import board as brd
import random as rnd

print("Let's start here")
newboard = brd.Board()
newboard.create()

vstee = 0
# todo: random player selection
vplayer = 'A'

while vstee < 8:
    if vstee == 0:
        vxp = rnd.randint(0,2)
        vyp = rnd.randint(0,2)
        vsymbol = 'X' if vplayer == 'A' else 'O'
        newboard[vxp][vyp] = vsymbol
        print(newboard.show())
    else:
        print("Tu bedzie else")
    print(vstee)
    vstee += 1


