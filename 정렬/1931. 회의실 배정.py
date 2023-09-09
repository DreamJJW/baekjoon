n = int(input())
schedule = []
for i in range(n):
    start, end = map(int, input().split())
    schedule.append((start, end))

schedule = sorted(schedule, key=lambda x: (x[1], x[0]))

time = 0
answer = 0

for j in schedule:
    if j[0] >= time:
        time = j[1]
        answer += 1

print(answer)