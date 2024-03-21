"""
randomly print numbers from 1 to 6  until number 1 appears

"""
import random
num=0
while num!=1:
    num=random.randint(1,6)
    print(num)
