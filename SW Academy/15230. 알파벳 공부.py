from string import ascii_lowercase
t = int(input())
s = list(ascii_lowercase)
for test_case in range(t):
    alp = input()
    cnt = 0
    for i in range(len(alp)):
        if alp[i] == s[i]:
            cnt += 1
        else:
            break

    print(f"#{test_case+1} {cnt}")
