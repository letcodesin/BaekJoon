from copy import deepcopy

board = []
for _ in range(4):
    info = list(map(int, input().split()))
    line = []
    i = 0
    while i < 7:
        line.append([info[i], info[i+1]-1])
        i += 2
    board.append(line)

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]

max_score = 0

#최댓값을 찾는 문제는 완전탐색을 필요로하므로 dfs사용
def dfs(shark_x, shark_y, score, board):
    global max_score
    score += board[shark_x][shark_y][0]
    max_score = max(score, max_score)
    shark_dirct = board[shark_x][shark_y][1]
    board[shark_x][shark_y] = [0,0]
    #print(board)

    #fish moving
    for fi in range(1, 17):
        fish_x = -1
        fish_y = -1
        fish_dirct = -1
        for x in range(4):
            for y in range(4):
                if board[x][y][0] == fi:
                    fish_x = x
                    fish_y = y
                    fish_dirct = board[x][y][1]
                    break
        if fish_x == -1 and fish_y == -1: #이미 먹힌 물고기인 경우
            continue
        for i in range(8):
            ndirct = (fish_dirct+i) % 8
            nx = fish_x + dx[ndirct]
            ny = fish_y + dy[ndirct]
            if not (0<=nx<4 and 0<=ny<4) or (nx == shark_x and ny == shark_y):
                continue
            board[fish_x][fish_y][1] = ndirct
            board[fish_x][fish_y], board[nx][ny] = board[nx][ny], board[fish_x][fish_y]
            break
    #print(board)

    for i in range(1,4):
        nx = shark_x + dx[shark_dirct]*i
        ny = shark_y + dy[shark_dirct]*i
        if 0<=nx<4 and 0<=ny<4 and board[nx][ny][0]>0:
            #dfs(nx, ny, score, board) #dfs를 수행할때 board값을 복사하지 않고 사용하면 board값이 잘못 저장됨
            dfs(nx, ny, score, deepcopy(board))

dfs(0,0,0,board)
print(max_score)

#참고: https://developer-ellen.tistory.com/68
