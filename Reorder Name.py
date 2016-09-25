

## reorder_name(name) reorders the name received in the order of Last name,
##    First name, and if there is, a first letter of the middle name

## reorder_name: Str -> Str
## required: name = Str with at least one " "

# Examples: reorder_name("William Henry Gates") => "Gates, William H"
#           reorder_name("elmer Fudd") => "Fudd, elmer"
#           reorder_name("a b c") => "c, a b"
import check


def reorder_name (name):
    if ((name.count(" "))== 1):
        first_name = name[0: (name.index(" "))]
        last_name = name[(1 + (name.index(" "))): (len(name))]
        return (last_name + ", " + first_name)
    elif ((name.count(" "))== 2):
        first_name = name[0: (name.index(" "))]
        last_name = last(name[(1 + (name.index(" "))): (len(name))])
        middle_name = middle(name[(1 + (name.index(" "))): (len(name))])
        return (last_name + ", " + first_name + " " + middle_name[0])

## last(name) produces a last name from the (name). (name) is a string of
##    middle name and last name
## last: Str -> Str
def last (name):
        first_name = name[0: (name.index(" "))]
        last_name = name[(1 + (name.index(" "))): (len(name))]
        return (last_name)
## middle(name) produces a middle name from the (name). (name) is a string of
##    middle name and last name
## middle: Str -> Str
def middle (name):
        middle_name = name[0: (name.index(" "))]
        last_name = name[(1 + (name.index(" "))): (len(name))]
        return (middle_name)

## Testing for reorder_name (name):
check.expect ("Test1", reorder_name("William Henry Gates"), "Gates, William H")
check.expect ("Test2", reorder_name("elmer Fudd"), "Fudd, elmer")
check.expect ("Test3", reorder_name("a b c"), "c, a b")
check.expect ("Test4", reorder_name("a bc"), "bc, a")
check.expect ("Test5", reorder_name("a b c d"), None)




