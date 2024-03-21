def binary():
    number = []
    num = int(input("Please enter your number: "))
    while num > 0:
        reminder = num % 2
        num = num // 2
        number.append(reminder)
    number.reverse()
    for i in range(len(number)):
        print(number[i], end='')


binary()


binary = input("Please enter your binary number: ")
length = len(binary)
decimal = 0
for i in range(0, length):
    current = int(binary[i])
    multi = 2 ** (length - (i + 1))*current
    decimal += multi
print(decimal)