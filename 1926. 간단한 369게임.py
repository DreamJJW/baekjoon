n = int(input())
temp = ''
for num in range(1, n + 1):
    if '3' in str(num) or '6' in str(num) or '9' in str(num):
        count_three = str(num).count('3')
        count_six = str(num).count('6')
        count_nine = str(num).count('9')
        temp = '-' * (count_three + count_six + count_nine)
        print(temp, end=' ')
    else:
        print(num, end=' ')