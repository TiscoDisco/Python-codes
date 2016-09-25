

## find_all(s, sub) finds every indices in s where sub is found. The output
##           comes out as a list of Integers

## find_all: Str Str -> (listof Nat)
## Required: s = Anyof Str
##           sub = Anyof Str

## Examples: find_all("og gogogog oGoo go", "go") => [3,5,7,16]
##           find_all("og gogogog oGoo go", "gogo") => [3,5]
##           find_all("A", "B") => []

## Body
import check
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

## Testing for find_all(s, sub):
check.expect ("TEST1", find_all("og gogogog oGoo go", "go"), [3,5,7,16])
check.expect ("TEST2", find_all("og gogogog oGoo go", "gogo"), [3,5])
check.expect ("TEST3", find_all("A", "B"), [])
check.expect ("TEST4", find_all("   ", " "), [0,1,2])
check.expect ("TEST5", find_all("ABC", "ABC"), [0])

