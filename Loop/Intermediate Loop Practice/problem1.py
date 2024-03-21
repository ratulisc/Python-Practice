# 1. You are given a list of numbers. print only the even numbers in sorted order
# input: 5  3 2 1 4 3 6 3 2 3 6
# output : 2 2 4 6 6


## Solution:

numbers = input().split()
numList = []
for i in range(len(numbers)):
    if (int(numbers[i]) % 2 == 0):
        numList.append(numbers[i])
sortedList = sorted(numList)
for a in range(len(numList)):
    print(sortedList[a],end = ' ')