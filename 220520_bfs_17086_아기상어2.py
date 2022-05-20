from collections import deque
n, m = map(int, input().split())
board = []
shark = deque()
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(m):
        if line[j] == 1:
            shark.append((i, j))
    board.append(line)
#print(board)
#print(shark)

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]

def bfs():
    while shark:
        x, y = shark.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if board[nx][ny] == 0:
                    shark.append((nx, ny))
                    board[nx][ny] = board[x][y] + 1
    return

bfs()
dist = 0
for i in range(n):
    for j in range(m):
        dist = max(dist, board[i][j])
print(dist - 1)

#참고: https://baejinsoo.github.io/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%20%EB%AC%B8%EC%A0%9C%ED%92%80%EA%B8%B0/BOJ_17086/
