##=======================================================
## Ryan Kim (20623928)
## CS 116 Winter 2016
## Assignment 06, Problem 2
##=======================================================

## munge_list(listStr) substitute all occrrences of certain letters in with
##         the listStrnumber of special character based on the chart provided.
##         Produces the list of strings with replaced characters. This function
##         mutates the values in listStr.
## Effects: Mutates the value in listStr based on the chart
## munge_list: (listof Str) -> None
##             listStr = ["a", "b"]
##             munge_list(listStr)
##             listStr = ["@", "8"]
## Required: listof Str = listof (Anyof Str)

## Examples: L = ["secret", "I Like Codes"]
##           munge_list(L) => None, L =>  ["$3(r3+", "! L!<3 (063$"]
##           L = ["password", "ANY yan", "123@#$"]
##           munge_list(L) => None, L => ["p@$$w0r6", "@N? ?@n", "123@#$"]
##           L = ["aaaab", "BBBbc"]
##           munge_list(L) => None, L => ["@@@@8", "8888("]

## Body
import check
def munge_list(listStr):
    listStr = count_munge(listStr, 0)

    

## count_munge(listStr, count) do recursive call for the list of Strings
## count_munge: (listof Str) Nat -> (listof Str)
def count_munge(listStr, count):
    if count == len(listStr):
        return (listStr)
    else:
        listStr[count] = (munger ((listStr[count]), 0))
        return (count_munge(listStr,count+1))

## munger(s, count) exchages each letter based on the chart given on the assignment
## munger: Str Nat -> Str
def munger (s, count):
    if count == len(s):
        return ("")
    else:
        if s[count].lower() == "a":
            return ("@" + (munger (s, count+1)))
        elif s[count].lower() == "b":
            return ("8" + (munger (s, count+1)))
        elif s[count].lower() == "c":
            return ("(" + (munger (s, count+1)))
        elif s[count].lower() == "d":
            return ("6" + (munger (s, count+1)))
        elif s[count].lower() == "e":
            return ("3" + (munger (s, count+1)))
        elif s[count].lower() == "f":
            return ("#" + (munger (s, count+1)))
        elif s[count].lower() == "g":
            return ("9" + (munger (s, count+1)))
        elif s[count].lower() == "h":
            return ("#" + (munger (s, count+1)))
        elif s[count].lower() == "i":
            return ("!" + (munger (s, count+1)))
        elif s[count].lower() == "k":
            return ("<" + (munger (s, count+1)))
        elif s[count].lower() == "o":
            return ("0" + (munger (s, count+1)))
        elif s[count].lower() == "q":
            return ("9" + (munger (s, count+1)))
        elif s[count].lower() == "s":
            return ("$" + (munger (s, count+1)))
        elif s[count].lower() == "t":
            return ("+" + (munger (s, count+1)))
        elif s[count].lower() == "v":
            return ("<" + (munger (s, count+1)))
        elif s[count].lower() == "x":
            return ("%" + (munger (s, count+1)))
        elif s[count].lower() == "y":
            return ("?" + (munger (s, count+1)))
        else:
            return(s[count] + (munger (s, count+1)))

## Testing for munge_list(listStr):
L = ["secret", "I Like Codes"]
check.expect("TEST1", munge_list(L), None)
check.expect("TEST1{L}", L, ["$3(r3+", "! L!<3 (063$"])
L = ["password", "ANY yan", "123@#$"]
check.expect("TEST2", munge_list(L), None)
check.expect("TEST2{L}", L, ["p@$$w0r6", "@N? ?@n", "123@#$"])
L = ["aaaab", "BBBbc"]
check.expect("TEST3", munge_list(L), None)
check.expect("TEST3{L}", L, ["@@@@8", "8888("])
L = ["abcdefghikoqstvxy"]
check.expect("TEST4", munge_list(L), None)
check.expect("TEST4{L}", L, ["@8(63#9#!<09$+<%?"])
L = ["ABCDEFGHIKOQSTVXY"]
check.expect("TEST5", munge_list(L), None)
check.expect("TEST5{L}", L, ["@8(63#9#!<09$+<%?"])
