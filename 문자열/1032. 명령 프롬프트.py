n = int(input())
order = list(input())
for i in range(n-1):
    temp_order = input()
    for j in range(len(order)):
        if order[j] == temp_order[j]:
            continue
        else:
            order[j] = '?'

print(*order, sep='')



