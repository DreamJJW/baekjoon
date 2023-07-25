N = int(input())
temp = []; a = ''
for i in str(N):
    temp.append(i)

temp.sort(reverse=True)

for j in temp:
    a += str(j)

print(a)

