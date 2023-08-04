t = int(input())
for i in range(t):
    num, alp = input().split()
    for j in alp:
        print(j * int(num), end='')
    print()
