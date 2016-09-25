

# min_dist (x1, y1, x2, y2, x3, y3) produces the shorstest distance for the
#   firends hang over among the three houses. Each (x,y) represent the
#   coordinates of three houses. Distances are measured through
#   Euclidean distance

# min_dist: Num Num Num Num Num Num -> String
# requires: all x1 ~ x3 and y1 ~ y3 >= 0

import check
import math

# Examples: min_dist (1,1,1,1,1,1) => "House1"
#           min_dist (1,1,10,10,10,10) => House2"



def min_dist (x1, y1, x2, y2, x3, y3):
    if (((math.sqrt(((x1-x2)**2) + ((y1-y2)**2)))
         > (math.sqrt(((x2-x3)**2) + ((y2-y3)**2))))
         and ((math.sqrt(((x1-x2)**2) + ((y1-y2)**2)))
         > (math.sqrt(((x1-x3)**2) + ((y1-y3)**2))))):
        return("House3")
    elif (((math.sqrt(((x2-x3)**2) + ((y2-y3)**2)))
            >= (math.sqrt(((x1-x3)**2) + ((y1-y3)**2))))
            and ((math.sqrt(((x2-x3)**2) + ((y2-y3)**2)))
            >= (math.sqrt(((x1-x2)**2) + ((y1-y2)**2))))):
        return("House1")
    else:
        return("House2")

# Testing min_dist:
check.expect("Test1", min_dist (1,1,1,1,1,1), "House1")
check.expect("Test2", min_dist (1,1,10,10,10,10), "House2")
check.expect("Test3", min_dist (1,2,3,4,5,6), "House2")
            

    
