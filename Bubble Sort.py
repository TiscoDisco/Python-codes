##=======================================================
## Ryan Kim (20623928)
## CS 116 Winter 2016
## Assignment 07, Problem 1
##=======================================================

## bubble_sort(lst) sorts the numbers in lst in descending order. This uses
##                  bubble method introduced in the assignment
## bubble_sort: (listof Num) -> (listof Num)

## Examples: bubble_sort([]) => []
##           bubble_sort([6, -5, 9]) => [9, 6, -5]
##           bubble_sort([ -9, 0, 66, 5, 3, 97,-34, 8, 21, 16]) => [97, 66, 21, 16, 8, 5, 3, 0, -9, -34]

import check
## Body
def bubble_sort(lst):
    if lst == []:
        return []
    else:
        return numVal(lst, (len(lst)-1))



## numVal(lst,count) returns the list from lst that is sorted descending
## numVal: (listof Num) Nat -> (listof Num)
def numVal(lst, count):
    if count == 0:
        return lst
    else:
        return numVal (order_change(lst, count, 0, 0), count-1)

## order_change(lst,numVal,space, count) returns the list from lst
##                                       that is sorted descending
## order_change: (listof Num) Nat Nat Nat -> (listof Num)
def order_change(lst, numVal, space, count):
    if count == numVal:
        return lst
    else:
        if lst[count] < lst[count+1]:
            space = lst[count]
            lst[count] = lst[count+1]
            lst[count+1] = space
            return order_change(lst, numVal, space, count+1)
        else:
            return order_change(lst, numVal, space, count+1)

## Testing for bubble_sort(lst):
check.expect("TEST1", bubble_sort([]), [])
check.expect("TEST2", bubble_sort([6, -5, 9]), [9, 6, -5])
check.expect("TEST3", bubble_sort([ -9, 0, 66, 5, 3, 97,-34, 8, 21, 16]), [97, 66, 21, 16, 8, 5, 3, 0, -9, -34])
check.expect("TEST4", bubble_sort([0,0,0,0,0]), [0,0,0,0,0])
check.expect("TEST5", bubble_sort([1]), [1])

