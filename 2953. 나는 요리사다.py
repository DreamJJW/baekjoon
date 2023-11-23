import sys

max_score = 0
winner = 0
for i in range(5):
    score = list(map(int, sys.stdin.readline().split()))
    if sum(score) > max_score:
        max_score = sum(score)
        winner = i + 1

print(winner, max_score)
