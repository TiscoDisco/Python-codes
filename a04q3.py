##=======================================================
## Ryan Kim (20623928)
## CS 116 Winter 2016
## Assignment 04, Problem 1
##=======================================================

# collatz_length (n) produces the number of steps that is required to get to one
#   using the Collatz method

# collatz_length: Num -> Num
# required: n != float n has to be positive

# Examples: collatz_length(2) => 1
#           collatz_length(42) => 8
import math
import check
def collatz_length (n):
    return length (n, 0)

# length(n, counter) uses the counter to count the number of recursions
#   that happened to get to one and returns the number
# length: Num Num -> Num
def length (n, counter):
    if n == 1:
        return counter
    else:
        if n%2 == 0:
            n = n/2
            return length (n, counter+1)
        else:
            n = 3 * n + 1
            return length (n, counter+1)

# Testing for length(n, counter):
check.expect("Test1", collatz_length(2), 1)
check.expect("Test2", collatz_length(42), 8)
check.expect("Test3", collatz_length(300), 16)
