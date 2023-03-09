stack = []
for i in range(5):
    num = int(input())
    stack.append(num)

stack.sort()
print((sum(stack)) // 5)
print(stack[2])
