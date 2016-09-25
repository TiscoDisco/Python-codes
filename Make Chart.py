##=======================================================
## Ryan Kim (20623928)
## CS 116 Winter 2016
## Assignment 06, Problem 4
##=======================================================

## chart(data) consumes list of strings and integers data and prints a chart based
##             on the strings and integers
##             layout rules:
##             Each bar label is right-aligned between two | symbols.
##             Each bar label ends one space before the right | symbol.
##             The longest bar label begins one space after the left | symbol.
##             Each bar is composed of # characters corresponding to the bar length in data.
##             Each bar begins immediately after the right | symbol.

## chart: (listof Str & Nat) -> None
##         function prints a chart made based on the rules
## Required: data = (listof Str & Nat)
##              ex) [Str Nat Str Nat Str Nat]

## Effects: This function prints a chart made based on the rules

## Examples: chart(["VW", 20, "Ford", 18, "Subaru", 3, "Mercedes", 7, "Fiat", 2]) => None
##           print"|       VW |####################
##                 |     Ford |##################
##                 |   Subaru |###
##                 | Mercedes |#######
##                 |     Fiat |##"
##           chart(["Label A", 11, "Label B", 3, "This is the longest label", 21]) => None
##           print"|                   Label A |###########
##                 |                   Label B |###
##                 | This is the longest label |#####################
##           chart(["A", 5, "B", 6, "AAA", 2])
##           print"|   A |#####
##                 |   B |######
##                 | AAA |##

## Body:
import check
def chart (data):
    produce_chart (data, 0, (highest_leng(data, 0, 0)))
    
## produce_chart (data, count, highest) prints the line based on the rules
## produce_chart: (listof Str & Nat) Nat Nat -> None
def produce_chart (data, count, highest):
    if count == (len(data)):
        return ("")
    else:
        print ("| " + (" " * (int(highest) - len(data[count]))) + \
               data[count] + " |" + ("#" * data[count+1]))
        produce_chart (data, count+2, highest)

## highest_leng (data,count,highest) gets the highest length of the string in the list
## highest_leng: (listof Str & Nat) Nat Nat -> Nat
def highest_leng (data, count, highest):
    if count == (len(data)):
        return highest
    else:
        if len(data[count]) > highest:
            highest = len(data[count])
            return (highest_leng(data, count+2, highest))
        else:
            return(highest_leng(data, count+2, highest))

## Testings for chart (data):
check.set_screen("Line 1: |                   Label A |########### Line 2: |                   Label B |### Line 3: | This is the longest label |#####################")
check.expect("TEST1", chart(["Label A", 11, "Label B", 3, "This is the longest label", 21]),None)
check.set_screen("Line1: |       VW |####################   Line2:|     Ford |################## Line3:|   Subaru |### Line4:| Mercedes |####### Lin5: |     Fiat |##")
check.expect("TEST2", chart(["VW", 20, "Ford", 18, "Subaru", 3, "Mercedes", 7, "Fiat", 2]), None)
check.set_screen("Line1:|   A |##### Line2:|   B |###### Line3:| AAA |##")
check.expect("TEST3", chart(["A", 5, "B", 6, "AAA", 2]), None)
check.set_screen("Line1:| A |### Line2:| B |### Line3:| C |###")
check.expect("TEST4", chart(["A", 3, "B", 3, "C", 3]), None)
check.set_screen("Line1:| A | Line2: |  | Line3: |   |")
check.expect("TEST5", chart(["A", 0, "", 0, " ", 0]), None)
             
                 
