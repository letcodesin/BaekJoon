r, c = map(int, input().split())
board = []
for _ in range(r):
    board.append(list(input()))
#print(board)
path = set()
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
cur_x = 0
cur_y = 0
path.add(board[cur_x][cur_y])
#dfs, backtracking
count = 0
max_count = 0
def dfs(cur_x, cur_y, count):
    global max_count
    max_count = max(count, max_count)
    if max_count == 26:#시간초과 방지
        return
    for i in range(4):
        if 0<= cur_x + dx[i] < r and 0<= cur_y + dy[i] < c:
            if board[cur_x + dx[i]][cur_y + dy[i]] not in path:
                path.add(board[cur_x + dx[i]][cur_y + dy[i]])
                dfs(cur_x + dx[i], cur_y + dy[i], count +1)
                path.remove(board[cur_x + dx[i]][cur_y + dy[i]])
dfs(0, 0, 1)
print(max_count)
# 참고: https://sorryhyeon.tistory.com/34
# 참고 bfs: https://velog.io/@nathan29849/BAEKJOON-1987-%EC%95%8C%ED%8C%8C%EB%B2%B3-DFS-python

