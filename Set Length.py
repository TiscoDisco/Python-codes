##=======================================================
## Ryan Kim (20623928)
## CS 116 Winter 2016
## Assignment 04, Problem 1
##=======================================================

## set_length(s,n) produces a string that is made out of s. n is a number of
##   spaces that a output string should have. If n is larger than
##   the length of s, output string starts again form the beginning of s.

# set_length: Str Nat -> Str
# required: n > 0

# Examples: set_length("It is snowing", 10) => "It is snow"
#           set_length("Python", 15) => "PythonPythonPyt"
#           set_length("abc", 5) => "abcabc"
import check

def set_length (s, n):
    if (len(s)) > n:
        return (set_length_count_small (s, n, 0))
    else:
        return (set_length_count_large (s, n, 0, 0))

# set_length_count_small (s, n, c) takes a case when the length of the string
#    is larger than n
# set_length_count_small: Str, Nat, Nat -> Str
def set_length_count_small (s, n, c):
    if c == (n - 1):
        return s[c]
    else:
        return (s[c] + (set_length_count_small(s,n,c+1)))
    
# set_length_count_large (s, n, c, c2) takes a case when the length of the string
#    is smaller than n
# set_length_count_large: Str, Nat, Nat, Nat -> Str
def set_length_count_large (s, n, c, c2):
    if c == len(s):
        c = 0
    if c2 == (n - 1):
        return s[c]
    else:
        return (s[c] + (set_length_count_large(s,n,c+1, c2 + 1)))

# Testing for set_length (s,n):
check.expect("Test1", set_length("It is snowing", 10), "It is snow")
check.expect("Test2", set_length("Python", 15), "PythonPythonPyt")
check.expect("Test3", set_length("abc", 5), "abcab")
check.expect("Test4", set_length(" ", 10), "          ")
check.expect("Test1", set_length("a", 200), "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")

