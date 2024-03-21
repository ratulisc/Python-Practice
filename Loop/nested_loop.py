t = int(input())
for a in range(t):
    n = int(input())
    for i in range(n):
        for j in range(n):
            print("*",end="")
        print()
    print()


###ChatGPT
# def draw_square(n):
#     for i in range(n):
#         for j in range(n):
#             print("*", end="")
#         print()
#
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     draw_square(n)
#     if _ < t - 1:  # Add a blank line between squares except for the last one
#         print()
