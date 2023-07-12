N = int(input())
answer = 1
room = 1    # 방 번호
cnt = 1     # 육각형 도는 카운트

while True:
    if N <= room:
        print(answer)
        break
    room += cnt * 6
    cnt += 1
    answer += 1



# while True:
#     cnt += 1
#     room += 1
#
#     if cnt == six:
#         six += 6
#         cnt = 0
#         answer += 1
#
#     if N == room:
#         print(answer)
#         break








