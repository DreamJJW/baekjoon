t = int(input())

# for i in range(t):
#     ps = input()
#     dict = {}
#     for j in ps:
#         if j not in dict:
#             dict[j] = 1
#         else:
#             dict[j] += 1
#     if ")" not in dict or "(" not in dict:
#         print("NO")
#     elif dict['('] == dict[')']:
#         print("YES")
#     else:
#         print("NO")

# '(' 와 ')' 괄호 숫자가 같으면 풀릴 줄 알았으나 '())(()' 테스트 케이스로 논파
# '()' 모양을 스택에 쌓고 확인해야 할 듯

for i in range(t):
    ps = input()
    stack = []
    for j in ps:
        if j == '(':
            stack.append(j)
        elif j == ')':
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    else:
        if not stack:
            print("YES")
        else:
            print("NO")





