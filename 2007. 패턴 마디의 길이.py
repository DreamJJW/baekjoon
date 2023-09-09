t = int(input())
for test_case in range(t):
    letter = input()

    for i in range(10, 1, -1):
        if letter[:i] == letter[i:i*2]:
            pattern = letter[:i]

    print(f"#{test_case + 1} {len(pattern)}")