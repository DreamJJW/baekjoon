n, c = map(int, input().split())
house = []
answer = 1

for i in range(n):
    x = int(input())
    house.append(x)

house.sort()

max_gap = house[-1] - house[0]
min_gap = house[1] - house[0]
gap = (max_gap + min_gap) // 2

idx = 0
while True:

    for i in range(len(house) - 1):
        if house[i + 1] >= house[idx] + gap:
            answer += 1
            idx = i + 1

    if answer < c:
        gap -= 1






