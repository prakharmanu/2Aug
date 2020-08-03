def detectCapitalUse(word):
    n = len(word)
    upper = 0
    for i in range(0,n):
        if word[i] >= "A" and word[i] <= "Z":
            upper += 1
    if ((upper == n or upper == 0) or (word[0] >= "A" and word[0] <= "Z" and upper == 1)):
            return True
    return False

word = "FlaG"
print(detectCapitalUse(word))