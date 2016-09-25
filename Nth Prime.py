

#nth_prime (n) produces the nth prime number starting from 2.

#nth_prime: Num -> Num
#Required: n has to be positive, n < 125

#Examples: nth_prime (1) => 2
#          nth_prime (5) => 11
import math
import check

def nth_prime (n):
    return prime_up(n, 2, 1)

#prime_up (n, start, counter) uses counter and starting number. Starting number
#  will become teh prime number by adding 1 everytime in every recursion
#prime_up: Num Num Num -> Num
def prime_up (n, start, counter):
    if n == counter-1:
        return start-1
    else:
        if prime_check(start,2) == True:
            return prime_up (n, start+1, counter+1) 
        else:
            return prime_up (n, start+1, counter)

# prime_check (n, counter) checks if the number is prime number
#prime_check: Num Num -> Bool
def prime_check (n, counter):
    if n > 1:
        if n == counter:
            return True
        elif n%counter == 0:
            return False
        else:
            return prime_check (n, counter+1)

# Testing for nth_prime:
check.expect("Test1", nth_prime (1), 2)
check.expect("Test2", nth_prime (5), 11)
check.expect("Test3", nth_prime (90), 463)

