class Node:
    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None

n = int(input())
for i in range(n):
    a, b = list(map(int, input().split()))
    