n, m = map(int, input().split())
name_list = []
no_see = []; no_hear = []

for i in range(n):
    name = input()
    no_see.append(name)

for j in range(m):
    name = input()
    no_hear.append(name)

name_list = sorted(set(no_see).intersection(no_hear))

print(len(name_list))
for name in name_list:
    print(name)