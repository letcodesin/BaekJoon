#########################solution########################
#각 세대 별 드레곤 커브 방향에 규칙 존재(이전세대 방향 거꾸로 뒤집어 + 1 한 것 % 4)
#0세대: 0
#1세대: 0 / 1
#2세대: 0 1 / 2 1
#3세대: 0 1 2 1 / 2 3 2 1
#4세대: 0 1 2 1 2 3 2 1 / 2 3 0 3 2 3 2 1
#식: (move[-i - 1] + 1) % 4

n = int(input())
board = [[0]*101 for _ in range(101)]
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for _ in range(n):
    x, y, d, gen = map(int, input().split())
    board[x][y] = 1
    move = [d]
    for g in range(gen):
        temp = []
        for i in range(len(move)):
            temp.append((move[-i-1]+1) % 4)
        move.extend(temp)

    for i in range(len(move)):
        nx = x + dx[move[i]]
        ny = y + dy[move[i]]
        board[nx][ny] = 1
        x, y = nx, ny
    
answer = 0
for i in range(100):
    for j in range(100):
        if board[i][j] and board[i+1][j] and board[i][j+1] and board[i+1][j+1]:
            answer += 1
print(answer)


#참고: https://kyun2da.github.io/2021/04/06/dragonCurve/
