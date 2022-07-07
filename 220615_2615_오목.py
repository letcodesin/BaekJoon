import sys
board = []
for _ in range(19):
    board.append(list(map(int, input().split())))

dx = [0, 1, 1, -1]
dy = [1, 0, 1, 1]

for x in range(19):
    for y in range(19):
        if board[x][y] != 0:
            color = board[x][y]
            for k in range(4):
                count = 1
                nx = x + dx[k]
                ny = y + dy[k]
                while 0<= nx <19 and 0<= ny <19 and board[nx][ny] == color:
                    count += 1
                    if count == 5:
                        if 0<= x-dx[k] <19 and 0<= y-dy[k] <19 and board[x-dx[k]][y-dy[k]] == color:
                            break
                        if 0<= nx+dx[k] <19 and 0<= ny+dy[k] <19 and board[nx+dx[k]][ny+dy[k]] == color:
                            break
                        print(color)
                        print(x+1, y+1)
                        sys.exit(0)                        
                    nx += dx[k]
                    ny += dy[k]
print(0)

'''
@ input
1 1 1 1 1 1
1 1 1 1 1 1
1 1 1 1 1 1
1 1 1 1 1 1
0 0 0 0 0 0
2 2 2 2 2 1
 
@ output
2
6 1

@wrong output
1
1 2
'''
#############################wrong solution#############################
import sys
board = []
for _ in range(19):
    board.append(list(map(int, input().split())))

def check_omok(i, j, color):
    if j+4 < 19:
        if board[i][j] == color and board[i][j+1] == color and board[i][j+2] == color and board[i][j+3] == color and board[i][j+4] == color:
            if j+5 < 19:
                if board[i][j+5] == color:
                    return False
            if j-1 >= 0:
                if board[i][j-1] == color:
                    return False             
            return True
    if i+4 < 19:
        if board[i][j] == color and board[i+1][j] == color and board[i+2][j] == color and board[i+3][j] == color and board[i+4][j] == color:
            if i+5 < 19:
                if board[i+5][j] == color:
                    return False
            if i-1 >= 0:
                if board[i-1][j] == color:
                    return False
            return True        
    if i+4 < 19 and j+4 < 19:
        if board[i][j] == color and board[i+1][j+1] == color and board[i+2][j+2] == color and board[i+3][j+3] == color and board[i+4][j+4] == color:
            if i+5 < 19 and j+5 < 19:
                if board[i+5][j+5] == color:
                    return False
            if i-1 >= 0 and j-1 >= 0:
                if board[i-1][j-1] == color:
                    return False
            return True
    if i-4 >= 0 and j+4 < 19:
        if board[i][j] == color and board[i-1][j+1] == color and board[i-2][j+2] == color and board[i-3][j+3] == color and board[i-4][j+4] == color:
            if i-5 >= 0 and j+5 < 19:
                if board[i-5][j+5] == color:
                    return False
            if i+1 < 19 and j-1 >= 0:
                if board[i+1][j-1] == color:
                    return False                
            return True

for i in range(19):
    for j in range(19):
        if board[i][j] == 1:
            if check_omok(i, j, 1):
                print(1)
                print(i+1, j+1)
                sys.exit(0)
        elif board[i][j] == 2:
            if check_omok(i, j, 2):
                print(2)
                print(i+1, j+1)
                sys.exit(0)
print(0)
