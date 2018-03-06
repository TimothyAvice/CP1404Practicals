"""
Random numbers
"""

import random

print(random.randint(5, 20))
print(random.randrange(3, 10, 2))
print(random.uniform(2.5, 5.5))

# 1) Smallest possible number is 5 and largest possible is 20 (Includes both end points)
# 2) Smallest number could of been 3 and largest would of been 9 (End point not included)
#   2a) No it goes up in steps of 2 so only 3, 5, 7 and 9 are possible
# 3) The smallest number possible is the start point (2.5) and the largest is just below the end point
