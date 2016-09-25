

## check_by_queen (queen_pos, king_pos) prduces "Check!!!" if king's position can be
##     attacked by the queen. Queen can moving infinite positions horizontally, vertically
##     diagonally

## check_by_queen: Str Str -> None
##                            print (anyof "Check!!!" nothing)
## Required: queen_pos and king_pos = (anyof A to H) + (anyof 1 to 8)

#Examples: check_by_queen ("E6", "A2") -> "Check!!!"
#          check_by_queen ("F2", "C2") -> "Check!!!"
#          check_by_queen ("A1", "H7") -> nothing

import check


def check_by_queen (queen_pos, king_pos):
    if (queen_pos[0] == king_pos[0]):
        return (print("Check!!!"))
    elif (queen_pos[1] == king_pos[1]):
        return (print ("Check!!!"))
    elif ((abs(int((converter(queen_pos))[0])) - (int((converter(king_pos))[0])))
          == (abs(int((converter(queen_pos))[1])) - (int((converter(king_pos))[1])))):
        return (print("Check!!!"))
            

## converter (pos) changes a string position vlaue in a different way
##    A = 1, B = 2, C = 3, D = 4, E = 5, F = 6, G = 7, H = 8

## converter: Str -> Str

def converter (pos):
    if (pos[0] == "A"):
        return ("1" + pos[1])
    elif (pos[0] == "B"):
        return ("2" + pos[1])
    elif (pos[0] == "C"):
        return ("3" + pos[1])
    elif (pos[0] == "D"):
        return ("4" + pos[1])
    elif (pos[0] == "E"):
        return ("5" + pos[1])
    elif (pos[0] == "F"):
        return ("6" + pos[1])
    elif (pos[0] == "G"):
        return ("7" + pos[1])
    elif (pos[0] == "H"):
        return ("8" + pos[1])

#Testing for check_by_queen(queen_pos, king_pos):

check.set_screen("Check!!!")
check.expect("TEST1", check_by_queen("E6", "A2"), None)
check.set_screen("Check!!!")
check.expect("TEST2", check_by_queen("F2", "C2"), None)
check.expect("TEST3", check_by_queen("A1", "H7"), None)
check.set_screen("Check!!!")
check.expect("TEST4", check_by_queen("F2", "F3"), None)
check.expect("TEST5", check_by_queen("F2", "G4"), None)



                
