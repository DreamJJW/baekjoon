t = int(input())
for test_case in range(t):
    s = input()
    sojung = 0
    for i in s:
        if i == 'o':
            sojung += 1

    answer = ''
    if (15 - len(s)) + sojung >= 8:
        answer = 'YES'
    else:
        answer = 'NO'

    print(f"{test_case+1} {answer}")