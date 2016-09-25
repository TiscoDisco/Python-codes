

## tomorrow (today) produces a string value of the day after today with a input
##    of today. If a string value does not belong in a week, produce unknown.

## tomorrow: Str -> (anyof "Monday" "Tuesday" "Wednesday" "Thursday" "Friday"
##       "Saturday" "Sunday" "Unknown")
## required: today = Any of String

#Examples: tomorrow("MoNday") -> "Tuesday"
#          tomorrow("TuesDay") -> "Wednesday"
#          tomorrow("MyBirthday") -> "Unknown"


import check


def tomorrow (today) :
    if ((today.lower()) == "monday"):
        return "Tuesday"
    elif ((today.lower()) == "tuesday"):
        return "Wednesday"
    elif ((today.lower()) == "wednesday"):
        return "Thursday"
    elif ((today.lower()) == "thursday"):
        return "Friday"
    elif ((today.lower()) == "firday"):
        return "Saturday"
    elif ((today.lower()) == "saturday"):
        return "Sunday"
    elif ((today.lower()) == "sunday"):
        return "Monday"
    else:
        return "Unknown"

# Testing for tomorrow(today):
check.expect("TEST1", tomorrow("MoNday"), "Tuesday")
check.expect("TEST2", tomorrow("TuesDay"), "Wednesday")
check.expect("TEST3", tomorrow("MoNday "), "Unknown")
check.expect("TEST4", tomorrow("MONDAY"), "Tuesday")
check.expect("TEST5", tomorrow(" fnweklfn"), "Unknown")
check.expect("TEST5", tomorrow("MyBirthday"), "Unknown")


