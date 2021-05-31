# Python3 code to demonstrate expression returns each integer
# from 1 to 25 exactly once
def eqProb():
    for first in range(1, 6):
        for second in range(1, 6):
            print(5 * first + second - 5)

eqProb()