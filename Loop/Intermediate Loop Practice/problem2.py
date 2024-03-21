# 2.You are given a list of numbers. Find the multiplication of all numbers
# input: 2 3 1 2 3
# output: 36

# Solution:


numbers = input().split()
numList = []
multi = 1
for i in range(len(numbers)):
    numList.append(int(numbers[i]))
    multi *= numList[i]
print(multi)

