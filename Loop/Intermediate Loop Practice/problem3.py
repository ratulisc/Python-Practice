# 3. You are given a list of numbers. Find the difference between the multiplication
# of the even numbers and the multiplication of odd numbers
# input: 1 2 3 4 2 3
# output : 7

#  Solution:


numbers = input().split()
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
evenList = []
oddList = []
multiOdd = 1
multiEven = 1
for i in range(len(numbers)):
    if (numbers[i] % 2 == 0):
        evenList.append(numbers[i])
        multiEven *= numbers[i]
    else:
        oddList.append(numbers[i])
        multiOdd *= numbers[i]
print(multiEven - multiOdd)

