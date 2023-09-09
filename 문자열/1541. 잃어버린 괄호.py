s = input()
s = s.split('-')

answer = 0
for i in s[0].split('+'):
    answer += int(i)

for j in s[1:]:
    for k in j.split('+'):
        answer -= int(k)


print(answer)