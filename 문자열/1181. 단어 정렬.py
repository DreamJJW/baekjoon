n = int(input())
words = []
for i in range(n):
    s = input()
    words.append(s)

words = set(words)
words = sorted(words, key=lambda x: (len(x), x))

for i in words:
    print(i)

