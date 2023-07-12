from collections import deque
import sys

N = int(input())
deck = deque()
for i in range(N):
    order = sys.stdin.readline().split()
    if order[0] == 'push_front':
        deck.appendleft(order[1])
    elif order[0] == 'push_back':
        deck.append(order[1])
    elif order[0] == 'pop_front':
        if not deck:
            print(-1)
        else:
            print(deck[0])
            deck.popleft()
    elif order[0] == 'pop_back':
        if not deck:
            print(-1)
        else:
            print(deck[-1])
            deck.pop()
    elif order[0] == 'size':
        print(len(deck))
    elif order[0] == 'empty':
        if deck:
            print(0)
        else:
            print(1)
    elif order[0] == 'front':
        if deck:
            print(deck[0])
        else:
            print(-1)
    elif order[0] == 'back':
        if deck:
            print(deck[-1])
        else:
            print(-1)



