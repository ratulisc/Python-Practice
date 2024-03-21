"""
you are given a number. now you have to check following conditions:
1. is the number greater than 10
2. is the number less than 50
3. is the number a even number
if all the condition is satisfied we call the number a "Little Genius Number"
otherwise it is a "Ordinary Number".

print what the number is.

"""


def check_little_genius(n):
    check=False
    if n>10 and n<50 and n%2==0:
        check=True


    return check

n=int(input("Please enter a number"))

if check_little_genius(n):
    print("It is a little genius")
else:
    print("An ordinary number")