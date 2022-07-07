board = []
for _ in range(5):
    board.append(list(map(int, input().split())))
num_list = []
for _ in range(5):
    num_list.append(list(map(int, input().split())))
#print(board)
#print(num_list)

def check_bingo(board):
    count = 0
    for i in range(5):
        if board[i].count(0) == 5:
            count += 1
    for i in range(5):
        if board[0][i] == 0 and board[1][i] == 0 and board[2][i] == 0 and board[3][i] == 0 and board[4][i] == 0:
            count += 1
    if board[0][0] == 0 and board[1][1] == 0 and board[2][2] == 0 and board[3][3] == 0 and board[4][4] == 0:
        count += 1
    if board[0][4] == 0 and board[1][3] == 0 and board[2][2] == 0 and board[3][1] == 0 and board[4][0] == 0:
        count += 1
    if count >= 3:
        return True
    return False
    

for i in range(25):
    for k in range(5):
        if num_list[i//5][i%5] in board[k]:
            findex = board[k].index(num_list[i//5][i%5])
            board[k][findex] = 0
            break
    if i >= 11 and check_bingo(board):
        print(i+1)
        break
            
