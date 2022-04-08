from collections import deque
from copy import deepcopy

n, m = map(int, input().split())
board = [list(map(int, input().split()))for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    virus_board = deepcopy(board)
    queue = deque()
    for i in range(n):
        for j in range(m):
            if virus_board[i][j] == 2:
                queue.append((i, j))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if virus_board[nx][ny] == 0:
                    virus_board[nx][ny] = 2
                    queue.append((nx, ny))
    safe_count = 0
    for i in range(n):
        safe_count += virus_board[i].count(0)
    global answer
    answer = max(answer, safe_count)

def makeWall(wall_count):
    if wall_count == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                board[i][j] = 1
                makeWall(wall_count + 1)
                board[i][j] = 0

answer = 0
makeWall(0)
print(answer)

#참고: https://hongcoding.tistory.com/m/130
