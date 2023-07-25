N = int(input())
dic = {}
for i in range(N):
    age, name = input().split()
    dic[name] = age

new_dic = sorted(dic.items(), key=lambda x:x[1])

for i, j in new_dic:
    print(j, i)

