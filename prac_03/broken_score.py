"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!

#score = float(input("Enter score: "))
#if score < 0:
#    print("Invalid score")
#else:
#    if score > 100:
#        print("Invalid score")
#    if score > 50:
#        print("Passable")
#    if score > 90:
#        print("Excellent")
#if score < 50:
#    print("Bad")

def score_checker(S):
    if S > 100:
        return "Invalid score"
    elif S > 90:
        return "Excellent"
    elif S > 50:
        return "Passable"
    elif S < 50:
        return "Bad"
    elif S < 0:
        return "Invalid score"


score = float(input("Enter score: "))
assesment = score_checker(score)
print(assesment)






