n = input("Please enter a number: ")
is_Palindrome = True
length = len(n)
for i in range(length // 2):
    if n[i] != n[length - 1 - i]:
        is_Palindrome = False
        break
if is_Palindrome:
    print("It is a Palindrome Number.")
else:
    print("It is not a Palindrome Number." )
