##=======================================================
## Ryan Kim (20623928)
## CS 116 Winter 2016
## Assignment 04, Problem 1
##=======================================================

# sum_of_digits (x) produce the sum of each number in each digits.
#    function takes out negative

# sum_of_digits: Num -> Num
# required: x != float

#Examples: sum_of_digits(1234) => 10
#          sum_of_digits(6789) => 30



import math
import check


def sum_of_digits (x):
    return sum_digits (x, 0)

# sum_digits (x, counter) uses the counter to add all the digits in n
#     adds one to the counter everytime runs the recursion
#  sum_digits: Num Num -> Num  
def sum_digits (x, counter):
    n = str(abs(x))
    length = len(n)    
    if counter == (length-1):
        return int(n[counter])
    else:
        return int(n[counter]) + sum_digits (x, counter + 1)


#Testing sum_of_digits:

check.expect ("Test1", sum_of_digits(1234), 10)
check.expect ("Test2", sum_of_digits(6789), 30)
check.expect ("Test3", sum_of_digits(00000), 0)
