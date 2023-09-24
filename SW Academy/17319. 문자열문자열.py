t = int(input())
for test_case in range(t):
    n = int(input())
    s = input()
    answer = ''

    if s[:n//2] == s[n//2:]:
        answer = "Yes"
    else:
        answer = "No"

    print(f"#{test_case+1} {answer}")

