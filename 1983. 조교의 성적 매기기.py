t = int(input())
rate = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
for test_case in range(t):
    n, k = map(int, input().split())
    temp = []
    for stu in range(n):
        score = list(map(int, input().split()))
        temp.append(score[0] * 0.35 + score[1] * 0.45 + score[2] * 0.20)

    student = temp[k-1] # 구하려는 학생의 점수 92.55000..
    temp = sorted(temp, reverse=True)
    idx = temp.index(student) // (n//10)

    print(f"#{test_case + 1} {rate[idx]}")

