N = int(input())
dimension = []
for i in range(N):
    x, y = list(map(int, input().split()))
    dimension.append((x, y))

new_dimension = sorted(dimension, key=lambda x : (x[0], x[1]))

for i, j in new_dimension:
    print(i, j)

