s = input()
croatia_alp = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in croatia_alp:
    s = s.replace(i, '*')

print(s)
print(len(s))