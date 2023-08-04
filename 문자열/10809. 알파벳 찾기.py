from string import ascii_lowercase
s = input()
alp = list(ascii_lowercase)
answer = [0] * 26

for i in range(26):
    if alp[i] in s:
        answer[i] = s.index(alp[i])
    else:
        answer[i] = -1

print(answer)
