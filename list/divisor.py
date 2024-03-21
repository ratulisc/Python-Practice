"""
Find all the divisor of n

"""

t = int(input())
for a in range(t):

    s= input().split()
    n1=int(s[0])
    n2=int(s[1])
    n3=int(s[2])
    numbers = []
    numbers.append(n1)
    numbers.append(n2)
    numbers.append(n3)
    numbers.sort()
    print("Case",a+1,end=': ')
    for i in range(len(numbers)):
        print(numbers[i],end=' ')
    print()




