t = int(input())

for i in range(t):

    s = input()
    vowels = []
    consonants = []
    for j in range(len(s)):
        if s[j] in "aeiouAEIOU":
            vowels.append(s[j])
        else:

            if s[j] == ' ': continue
            consonants.append(s[j])

    for i in range(len(vowels)):
        print(vowels[i], end='')
    print()
    for i in range(len(consonants)):
        print(consonants[i], end='')
    print()
