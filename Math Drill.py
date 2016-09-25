

## math_drill(listofQues) getting a listofQues consist of strings.
##        Each string is a mathmetical equation. If a input from
##        the user gets the right answer, print "Correct" and returns
##        number of correct answers at the end

## math_drill: (listof Str) -> Nat
## Required:  listofQues = listof Str
##            Str = form of "number (anyof "+" "-" "*") number"

## Effects: Gets an input from the user, if the answer is correct
##          print "Correct", wrong print "Wrong".

## Examples: math_drill(["1 + 1", "3 * 5", "1000 - 1"]) =>
##           input("What is 1 + 1?" 2)
##           print "Correct"
##           input("What is 3 * 5?" 20)
##           print "Wrong"
##           input ("What is 1000 - 1" 999)
##           print "Correct"
##           return 2
##           math_drill(["100 * 5", "222 - 32"]) =>
##           input("What is 100 * 5" 50)
##           print "Wrong"
##           input("What is 222 - 32?" 191)
##           print "Wrong"
##           return 0
##           math_drill(["1 + 1", "2 * 2"])
##           input("What is 1 + 1?" 2)
##           print "Correct"
##           input("What is 2 * 2?" 4)
##           print "Correct"
##           return 2


## Body:
import check
def math_drill(listofQues):
    return (Ask (listofQues, 0, 0))

## Ask(listofQues, count, correct) check in the user entered the question right
## Ask: (listof Str) Nat Nat -> Nat
def Ask (listofQues, count, correct):
    if count == len(listofQues):
        return correct
    else:
        if (int(input("What is " + listofQues[count] + "?"))) \
           == int(answer_finder(listofQues[count])):
            print("Correct")
            correct += 1
            return (Ask (listofQues, count+1, correct))
        else:
            print("Wrong")
            return (Ask (listofQues, count+1, correct))


## answer(Ques, count) gets the indice of the space
## answer: Str Nat -> Nat
def answer (Ques, count):
    if Ques[count] == " ":
            return count
    else:
            return (answer (Ques, count+1))

## answer_finder(Ques) gets the answer of the Question
## answer_finder: Str -> Nat
def answer_finder (Ques):
            space = answer(Ques, 0)
            firstNum = int(Ques[0:space])
            secondNum = int(Ques[space+3:len(Ques)])
            if Ques[space+1:space+2] == "+":
                return (firstNum + secondNum)
            elif Ques[space+1:space+2] == "-":
                return (firstNum - secondNum)
            elif Ques[space+1:space+2] == "*":
                return (firstNum * secondNum)

## Testings for math_drill(listofQues):
L = ["1 + 1", "3 * 5", "1000 - 1"]
check.set_input(['2','20','999'])
check.set_screen('Correct\nWrong\nCorrect')
check.expect("TEST1", math_drill(L), 2)
L = ["100 * 5", "222 - 32"]
check.set_input(['20','191'])
check.set_screen('Wrong\nWrong')
check.expect("TEST2", math_drill(L), 0)
L = ["1 + 1", "2 * 2"]
check.set_input(['2','4'])
check.set_screen('Correct\nCorrect')
check.expect("TEST3", math_drill(L), 2)
L = ["44 - 33", "1000 - 1000", "0 - 2"]
check.set_input(['11','0','-2'])
check.set_screen('Correct\nCorrect\nCorrect')
check.expect("TEST4", math_drill(L), 3)
L = ["1 + 1"]
check.set_input(['0'])
check.set_screen('Wrong')
check.expect("TEST5", math_drill(L), 0)
