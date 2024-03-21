import math
t = int(input())
for i in range(t):
    s = input().split()
    slen = len(s)
    fact = 1
    count = 1
    s = sorted(s)
    for j in range(slen-1):
        next = s[j+1]
        current = s[j]
        
        countList = [ ]
        
        if next == current :
            count += 1
            
        else:
            countList.append(count)
            count = 1
        
        if j == slen-2:
            countList.append(count)
            
        for a in range(len(countList)):
            fact = fact * math.factorial(countList[a])
        result = math.factorial(slen) / fact
    print("1/",end = "")
    print(int(result))