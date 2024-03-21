"""
Problem 1: Calculate sum of  100 number and multiplication of 100 number in a same loop.


Problem 2: Write a code that take two input a,b and prints sum of all values from a to b.

Problem 3: Write a code that takes two integer a,b and a string s which can be either "inclusive" or "exclusive".
            if s is "inclusive" print the sum of a to b including a and b.otherwise print the sum of a to b excluding
             a and b.
"""
#Solution 3:

a = int(input("Pleae enter first number: "))
b = int(input("Please enter second number: "))
string = input("Please enter is inclusive or exclusive: ")
sum = 0
if string == "inclusive":
    for i in range(a,b+1):
        sum+=i

elif string == "exclusive":
    for i in range(a+1,b):
        sum+=i

print(sum)





















# Solution:







# sum=0
# multiplication=1
# for i in range(1,101):
#     sum+=i
#     multiplication*=i
#
#
# print("Multiplication is: ",multiplication)
# print("Sum is ", sum)
sum=0
# a=int(input("Enter first number: "))
# b=int(input("Enter second number: "))
# for i in range(a,b+1):
#     sum+=i
# print(sum)






