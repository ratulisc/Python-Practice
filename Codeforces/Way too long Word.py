t = int(input())
for i in range(t):
    string = input()
    length = len(string)
    if length > 10:
        print(string[0], end='')
        print(length - 2, end='')
        print(string[length - 1], end='')
        print()
    else:
        print(string)
