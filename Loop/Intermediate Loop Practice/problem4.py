# 4. You are given a string find the sum of ascii code of all the alphabets.
# input: ab 
# output: 131


#  Solution:


strings = input()
sums = 0
for i in range(len(strings)):
    sums += ord(strings[i])
print(sums)