n = int(input())
x = set(map(int, input().split()))
m = int(input())
y = list(map(int, input().split()))

for i in y:
    if i in x:
        print('1')
    else:
        print('0')
