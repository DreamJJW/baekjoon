n = int(input())
for i in range(n):
    test = list(input())
    right = []
    left = []
    for i in test:
        if i == '-':
            if left:
                left.pop()
        elif i == '<':
            if left:
                right.append(left.pop())
        elif i == '>':
            if right:
                left.append(right.pop())
        else:
            left.append(i)
    left.extend(right)
    print("".join(left))
