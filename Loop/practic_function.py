"""
you are given a number. now you have to check following conditions:
1. is the number greater than 10000
2. is the number an odd number
if all the condition is satisfied we call the number a "Fat Genius"
otherwise it is an "Ordinary Number".

print what the number is?
"""


def fat_genius(a):
    check = False
    if a > 10000 and a % 2 != 0:
        check = True
    return check


n = int(input("Please enter a number: "))
if fat_genius(n):
    print("Fat Genius")
else:
    print("Ordinary Numbers")
