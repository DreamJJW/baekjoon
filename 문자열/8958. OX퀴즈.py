t = int(input())
for i in range(t):
    quiz = input()
    score = 0
    temp = 0
    for ox in quiz:
        if ox == 'O':
            temp += 1
            score += temp
        else:
            temp = 0
    print(score)


