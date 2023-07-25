N = int(input())
P = list(map(int, input().split()))
a = 0; temp = []
P.sort()
for i in P:
    a += i
    temp.append(a)

print(sum(temp))

