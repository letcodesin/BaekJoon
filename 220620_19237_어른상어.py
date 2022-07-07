n, m, k = map(int, input().split())
shark_board = []
for _ in range(n):
    shark_board.append(list(map(int, input().split())))
shark_direct = list(map(int, input().split()))
direct_priority = []
for i in range(m):
    plist  = []
    for _ in range(4):
        plist.append(list(map(int, input().split())))
    direct_priority.append(plist)
smell = [[[0,0]for _ in range(n)]for _ in range(n)]
def update_smell():
    for i in range(n):
        for j in range(n):
            if smell[i][j][1] > 0:
                smell[i][j][1] -= 1
            if shark_board[i][j] != 0:
                smell[i][j] = [shark_board[i][j],k]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def shark_move():
    new_shark_board = [[0 for _ in range(n)]for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if shark_board[i][j] != 0:
                direct = shark_direct[shark_board[i][j]-1]
                found = False
                for k in range(4):
                    idx = direct_priority[shark_board[i][j]-1][direct-1][k]
                    nx = i + dx[idx - 1]
                    ny = j + dy[idx - 1]
                    if 0<= nx <n and 0<= ny <n and smell[nx][ny][1] == 0:
                        shark_direct[shark_board[i][j]-1] = idx
                        if new_shark_board[nx][ny] == 0:
                            new_shark_board[nx][ny] = shark_board[i][j]
                        else:
                            new_shark_board[nx][ny] = min(new_shark_board[nx][ny], shark_board[i][j])
                        found = True
                        break
                if found:
                    continue
                #주위에 빈칸이 없는 경우, 자신의 냄새가 있는 곳으로 이동
                for k in range(4):
                    idx = direct_priority[shark_board[i][j]-1][direct-1][k]
                    nx = i + dx[idx - 1]
                    ny = j + dy[idx - 1]
                    if 0<= nx <n and 0<= ny <n and smell[nx][ny][0] == shark_board[i][j]:
                        shark_direct[shark_board[i][j]-1] = idx
                        new_shark_board[nx][ny] = shark_board[i][j]
                        break
    return new_shark_board

time = 0
while True:
    update_smell()
    new_shark_board = shark_move()
    shark_board = new_shark_board
    time += 1
    check_only = True
    for i in range(n):
        for j in range(n):
            if shark_board[i][j] > 1:
                check_only = False
    if check_only:
        print(time)
        break
    if time >= 1000:
        print(-1)
        break
