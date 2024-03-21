"""
functions in list:
1.insert
2.append
3.pop
4.index
5.sort
6.find



"""

""""# def printlist(mylist):
#     for i in range(len(mylist)):
#         print(mylist[i],end=' ')
#     print()
#
# mylist=[]
# for i in range(1,6):
#     mylist.append(i)


# t = int(input())
# for i in range(t):
#    numbers=input().split()
#    print(len(numbers))"""

import math

t = int(input())
num = int(input())
for i in range(t):
    for i in range(i):
        root = math.sqrt(num)
        var = int(root)
        if var**2==num:
            print("YES")
        else:
            print("NO")

