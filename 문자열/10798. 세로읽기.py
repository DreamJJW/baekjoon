board = []
temp = []
for i in range(5):
    word = input()
    board.append(word)
    temp.append(len(word))

for i in range(len(board)):
    for j in range(len(board[i])):
        print(board[j][i], end='')
    print()

