from collections import deque
import sys
input = sys.stdin.readline #시간단축시 필요

n, l, r = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[-1 for _ in range(n)]for _ in range(n)]
count = 0
candidate = deque()
for i in range(n):
    for j in range(i%2, n, 2):
        candidate.append((i, j))
#print(candidate)
while True:
    queue = deque()
    for _ in range(len(candidate)):
        i, j = candidate.popleft()
        if visited[i][j] == count:
            continue
        visited[i][j] = count
        ulist = set([(i, j)])
        sum = board[i][j]
        queue.append((i, j))

        while queue:
            x, y = queue.popleft()
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if nx>=n or nx<0 or ny>=n or ny<0 or visited[nx][ny] == count:
                    continue
                if l<=abs(board[x][y]-board[nx][ny])<=r:
                    visited[nx][ny] = count
                    ulist.add((nx, ny))
                    sum += board[nx][ny]
                    queue.append((nx, ny))
        if len(ulist) > 1:
            mean = sum // len(ulist)
            for x, y in ulist:
                board[x][y] = mean
                candidate.append((x, y))
            #print(board)
    if candidate:
        #print(candidate, count)
        count += 1
    else:
        break
print(count)

#참고: https://my-coding-notes.tistory.com/443

'''
####################시간 초과 풀이########################
from collections import deque
import sys
input = sys.stdin.readline
n, l, r = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j):
    queue = deque()
    ulist = []
    queue.append((i,j))
    ulist.append((i,j))
    while queue:
        point = queue.popleft()
        for k in range(4):
            nx = point[0] + dx[k]
            ny = point[1] + dy[k]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny] == 0:
                if l<=abs(board[point[0]][point[1]]-board[nx][ny])<=r:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                    ulist.append((nx, ny))
    return ulist

count = 0
while True:
    visited = [[0 for _ in range(n)]for _ in range(n)]
    check_change = False
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                visited[i][j] = 1
                ulist = bfs(i, j)
                if len(ulist) > 1:
                    #print(count)
                    check_change = True
                    #print(ulist)
                    sum = 0
                    for z in range(len(ulist)):
                        sum += board[ulist[z][0]][ulist[z][1]]
                    mean = sum // len(ulist)
                    for z in range(len(ulist)):
                        board[ulist[z][0]][ulist[z][1]] = mean
                    #print(board)
    if check_change == False:
        break
    count += 1
print(count)            
'''
'''
########################틀린 풀이#########################
n, l, r = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
print(board)

count = 0
while True:
    ulist = []
    for i in range(n):
        for j in range(n-1):
            if l <= abs(board[i][j]-board[i][j+1]) <= r:
                ulist.append((i,j))
                ulist.append((i,j+1))

    for j in range(n):
        for i in range(n-1):
            if l <= abs(board[i][j]-board[i+1][j]) <= r:
                ulist.append((i,j))
                ulist.append((i+1,j))
    ulist = set(ulist)
    ulist = list(ulist)
    ulist.sort(key = lambda x: (x[0], x[1]))
    print(ulist)

    if len(ulist) == 0:
        break

    union = [[ulist[0]]]
    for i in range(1, len(ulist)):
        mdiff = 5
        for j in range(len(union)):
            for k in range(len(union[j])):
                diff =  abs(ulist[i][0] - union[j][k][0]) + abs(ulist[i][1] - union[j][k][1])
                mdiff = min(mdiff, diff)
            if mdiff == 1:
                union[j].append(ulist[i])
            else:
                union.append([ulist[i]])
    print(union)

    for j in range(len(union)):
        sum = 0
        for k in range(len(union[j])):
            sum += board[union[j][k][0]][union[j][k][1]]
        mean = sum // len(union[j])
        for k in range(len(union[j])):
            board[union[j][k][0]][union[j][k][1]] = mean
    print(board)
    count += 1
print(count)
'''