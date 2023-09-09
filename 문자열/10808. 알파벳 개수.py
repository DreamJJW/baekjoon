from string import ascii_lowercase
s = input()
alp = ascii_lowercase
temp = [0] * 26

for i in range(26):
    if alp[i] in s:
        temp[i] = s.count(alp[i])

print(*temp)

