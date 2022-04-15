from copy import deepcopy
r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]
#print(board)

dx = [1, 1, 1]
dy = [-1, 0, 1] #우상향, 직진, 우하향 순으로 파이프를 설치해야 가장 많아짐
count = 0

def dfs(y, x, pipe_board):
    pipe_board[y][x] = '0'
    if x == c-1:
        #print(pipe_board)
        return True
    for i in range(3):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<c and 0<=ny<r:
            if pipe_board[ny][nx] == '.':
                if dfs(ny, nx, pipe_board):#dfs로 끝까지 설치가능한 경우만 설치
                    return True
    return False

count = 0
pipe_board = deepcopy(board)
for i in range(r):
    if dfs(i, 0, pipe_board):
        count += 1
print(count)

#참고: https://inspirit941.tistory.com/249