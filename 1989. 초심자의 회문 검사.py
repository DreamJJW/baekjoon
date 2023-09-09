t = int(input())
for test_case in range(t):
    word = input()
    if word == word[::-1]:
        answer = 1
    else:
        answer = 0

    print(f"#{test_case+1} {answer}")