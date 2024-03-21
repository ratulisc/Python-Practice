t = int(input())
for a in range(t):
    factorial = int(input())
    ans = 1
    for i in range(2, factorial + 1):
        ans *= i
    print(ans)
