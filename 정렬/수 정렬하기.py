n = int(input())
stack = []

for i in range(n):
    num = int(input())
    stack.append(num)

stack.sort()
for i in stack:
    print(i)