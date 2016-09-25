

## word_count(string) prints number of each word in string. Case sensitive.
##             print follows the format given in the assignment The output is
##             sorted alphabetically.
## word_count: Str -> None
## Effects: prints out number of each word

## Examples:
## word_count(“Up,up,up,to the sky, 3 ups.”) => None
## prints “There are a total of 8 words.
##3 - 1 times.
##Up - 1 times.
##sky - 1 times.
##the - 1 times.
##to - 1 times.
##up - 2 times.
##ups - 1 times.”
## word_count("mixed-with-symbols!!! hi2342648 @#$%^&*") => None
## prints “There are a total of 3 words.
## @#$%^&* - 1 times.
## hi2342648 - 1 times.
## mixed-with-symbols!!! - 1 times."
## word_count("	"Once upon a time, there was a mountain. In the mountain, there
##was a temple. In the temple, there was an old monk. The old monk was
##telling a story to a young monk. The story went like this, once upon a
##time, there was a mountain...",) => None
## prints “There are a total of 47 words.
##In - 2 times.
##Once - 1 times.
##The - 2 times.
##a - 7 times.
##an - 1 times.
##like - 1 times.
##monk - 3 times.
##mountain - 3 times.
##old - 2 times.
##once - 1 times.
##story - 2 times.
##telling - 1 times.
##temple - 2 times.
##the - 2 times.
##there - 4 times.
##this - 1 times.
##time - 2 times.
##to - 1 times.
##upon - 2 times.
##was - 5 times.
##went - 1 times.
##young - 1 times.”
import check
## Body
def word_count(string):
    if string == "":
        print ("There are a total of 0 words.")
    else:
        print ("There are a total of " + str(len(list_create(remover(string), 0, [], find_all(remover(string), " ")))) + " words.")
        print_func(string, 0, list_create(remover(string), 0, [], find_all(remover(string), " ")))

## print_func(string, count, lst) prints the number of times each word in string
## print_func: Str Nat (listof Str) -> None
## Effects: prints out number of times each word in string
def print_func(string, count, lst):
    if count == len(lst):
        return None
    else:
        print(lst[count] + " - " +  str(string.count(lst[count])) + " times.")
        return print_func(string, count +1, lst)

## remover(string) removes "," and "." from the string
## remover: Str -> Str
def remover(string):
    s = string.replace(",","")
    s = s.replace(".","")
    return s

## list_create(string, count, lst, space_lst) produces the list of words forming
##            string
## list_create: Str Nat (listof Str) (listof Num)
def list_create(string, count, lst, space_lst):
    if count == len(space_lst):
        lst.append(string[0:len(string)])
        return sorted(set(lst))
    else:
        lst.append(string[0:string.index(" ")]) 
        string = string[string.index(" ")+1:len(string)]
        return list_create(string, count+1, lst, space_lst)




## find_all: Str Str -> (listof Nat)
## Required: s = Anyof Str
##           sub = Anyof Str
def find_all(s, sub):
    l = []
    return (find_help(s, sub, 0, l))

## find_help(s, sub, count, list2) is a helper function that produces list of
##     Integers that are indices of sub in s

## find_help: Str Str Nat (listof Nat) -> (listof Nat)
def find_help(s, sub, count, list2):
    if (count == ((len(s) - len(sub))+1)):
        return(list2)
    else:
        if (s[count:(count + len(sub))] == sub):
            list2.append(count)
            return (find_help(s, sub, count+1, list2))
        else:
            return (find_help(s, sub, count+1, list2))

## Testing for word_count(string):
check.expect("TEST1", word_count("Up,up,up,to the sky, 3 ups."), None)
check.set_screen("There are a total of 8 words.3 - 1 times.Up - 1 times.sky - 1 times.the - 1times.to - 1 times.up - 2 times.ups - 1 times.")
check.expect("TEST2", word_count("mixed-with-symbols!!! hi2342648 @#$%^&*"), None)
check.set_screen("There are a total of 3 words. @#$%^&* - 1 times. hi2342648 - 1 times. mixed-with-symbols!!! - 1 times.")
check.expect("TEST3", word_count("Once upon a time, there was a mountain. In the mountain, there was a temple. In the temple, there was an old monk. The old monk was telling a story to a young monk. The story went like this, once upon a time, there was a mountain..."), None)
check.expect("TEST4", word_count(""), None)
check.set_screen("There are a total of 0 words.")

