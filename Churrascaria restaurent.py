##=======================================================
## Ryan Kim (20623928)
## CS 116 Winter 2016
## Assignment 07, Problem 4
##=======================================================

## churras(status, dice) prints churrascaria way of restaurents with its
##       positions as status and dice rolls as dice
##       follows the rules shown on the assignment
## churras: (listof Str) (listof Nat) -> None
## Effect: prints steps for its status and ending comment
## Restriction: status = (listof (anyof 'green' 'red'))

## Examples:
## churras(['red', 'green', 'green', 'green'],[11,4,12,3,10])
## => None
## prints
## ['red', 'green', 'green', 'green']
## ['green', 'green', 'green', 'green']
## Let's eat. We are all very very hungry!
## churras(['red','red','green','green'], [7,8,8,11,6])
## => None
## prints
## ['red', 'red', 'green', 'green']
## [‘red’, 'green', 'green', 'green']
## ['green', 'green', 'green', 'green']
## Let's eat. We are all very very hungry!
## churras(['green','red','red','red'], [11,3,5,7,10])
## => None
## ['green','red','red','red']
## ['red', 'green', 'red', 'green']
## ['green', 'red', 'green', 'green']
## ['green', 'red', 'red', 'green']
## ['green', 'red', 'green', red']
## ['red','red','red','red']
## Let's eat. We are all very very hungry!

import check
## Body
def churras (status, dice):
    dance(status, dice, 0)

## dance(status, dice, count) runs the basic rules of churras and prints output
## dance: (listof Str) (listof Nat) Nat -> None
## Effects: prints steps for its status and ending comment
def dance(status, dice, count):
    if status_check(status, 0):
        print("Let's eat. We are all very very hungry!")
    elif count == 0:
        print (status)
        status[0] = 'green'
        status[2] = 'green'
        status = rotate(status, 0, (dice[count] % 4))
        print (status)
        dance(status, dice, count +1)
    elif count == 1:
        status[0] = 'green'
        status[1] = 'green'
        status = rotate(status, 0, (dice[count] % 4))
        print (status)
        dance(status, dice, count +1)
    elif count == 2:
        if status[0] == 'green' and status[2] == 'green':
            status[0] = 'red'
        else:
            status[0] = 'green'
            status[2] = 'green'
        status = rotate(status, 0, (dice[count] % 4))
        print (status)
        dance(status, dice, count +1)
    elif count == 3:
        if status[0] == 'green':
            status[0] = 'red'
        elif status[0] == 'red':
            status[0] = 'green'
        if status[1] == 'green':
            status[1] = 'red'
        elif status[1] == 'red':
            status[1] = 'green'
        status = rotate(status, 0, (dice[count] % 4))
        print (status)
        dance(status, dice, count +1)
    elif count == 4:
        if status[0] == 'green':
            status[0] = 'red'
        elif status[0] == 'red':
            status[0] = 'green'
        if status[2] == 'green':
            status[2] = 'red'
        elif status[2] == 'red':
            status[2] = 'green'
        status = rotate(status, 0, (dice[count] % 4))
        print (status)
        print ("Let's eat. We are all very very hungry!")


## rotate(status, count, dice) changes the status order based on dice
## rotate: (listof Str) Nat Nat -> (listof Str)
def rotate(status, count, dice):
    if count == dice:
        return status
    else:
        status = [status[-1]] + status[0:-1]
        return rotate(status, count+1, dice)

## status_check(status, count) checks if all the values in status are the same
## status_check: (listof Str) Nat -> Bool
def status_check(status, count):
    if len(status)-1 == count:
        return True
    elif status[count] != status[count+1]:
        return False
    else:
        return status_check(status, count+1)

## Testing for churras(status, dice)
check.expect("TEST1", churras(['red', 'green', 'green', 'green'],[11,4,12,3,10]), None)
check.set_screen("['red', 'green', 'green', 'green']['green', 'green', 'green', 'green']Let's eat. We are all very very hungry!")
check.expect("TEST2", churras(['red','red','green','green'], [7,8,8,11,6]), None)
check.set_screen("['red', 'red', 'green', 'green'][‘red’, 'green', 'green', 'green']['green', 'green', 'green', 'green']Let's eat. We are all very very hungry!")
check.expect("TEST3", churras(['green','red','red','red'], [11,3,5,7,10]), None)
check.set_screen("['green','red','red','red']['red', 'green', 'red', 'green']['green', 'red', 'green', 'green']['green', 'red', 'red', 'green']['green', 'red', 'green', red']['red','red','red','red']Let's eat. We are all very very hungry!")
check.expect("TEST4", churras(['red', 'red', 'red', 'red'], [12,12,12,12,12]), None)
check.set_screen("['red', 'red', 'red', 'red'] Let's eat. We are all very very hungry!")

 
