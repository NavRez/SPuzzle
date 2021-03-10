# make a DFS algorithm for the S Puzzle
# to do so, you will need to start out with the smallest index value and go to the greatest
# prioritize left, down, right and up in that order : make sure these are functions
# make it recursive

def RecurseTest(integer):
    if integer > 1:
        RecurseTest(integer-1)
    print(integer)

RecurseTest(integer=10)

