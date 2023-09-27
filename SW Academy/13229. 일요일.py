t = int(input())
days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
for test_case in range(t):
    s = input()

    if s == "SUN":
        answer = 7
    else:
        answer = 7 - (days.index(s) + 1)

    print(f"#{test_case+1} {answer}")

