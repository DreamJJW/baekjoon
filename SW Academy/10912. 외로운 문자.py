t = int(input())
for test_case in range(t):
    s = input()
    s = sorted(s)

    temp = []
    for i in range(len(s)):
        if temp:
            if s[i] in temp:
                temp.pop()
            else:
                temp.append(s[i])
        else:
            temp.append(s[i])

    if temp:
        answer = "".join(temp)
    else:
        answer = "Good"

    print(f"#{test_case+1} {answer}")