def checker(word):
    temp = []
    temp.append(word[0])
    for i in range(1, len(word)):
        if word[i] != word[i - 1]:
            temp.append(word[i])

    if len(temp) == len(set(temp)):
        return True

    return False

n = int(input())
cnt = 0
for j in range(n):
    s = input()
    if checker(s):
        cnt += 1
print(cnt)
