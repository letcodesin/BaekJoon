from collections import deque
r,c,n = map(int,input().split())
data = [list(input()) for _ in range(r)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]
q = deque()

def bfs(q,data):
    while q:
        x,y = q.popleft()
        data[x][y] = '.'
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0<=nx<r and 0<=ny<c and data[nx][ny]=='O':
                data[nx][ny] = '.'

def simulate(time):
    global data, q
    if time == 1:
        for i in range(r):
            for j in range(c):
                if data[i][j] == 'O':
                    q.append((i,j))
    elif time % 2 == 1:
        bfs(q,data)
        for x in range(r):
            for y in range(c):
                if data[x][y] == 'O':
                    q.append((x,y))
    else:
        data = [['O']*c for _ in range(r)]

for i in range(1,n+1):
    simulate(i)

for row in data:
    print(''.join(row))

#참고: https://jae-eun-ai.tistory.com/15

#####################worng solution########################

R, C, N = map(int,input().split())
graph = []
for i in range(R):
    line = list(input())
    graph.append(line)

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

if N % 2 == 0:
    for i in range(R):
        line = ""
        for j in range(C):
            line += "0"
        print(line)
elif (N-3) % 4 == 0:
    for i in range(R):
        line = ""
        for j in range(C):
            exist_boom = False
            if graph[i][j] == "0":
                exist_boom = True
            for k in range(4):
                new_r = i+dr[k]
                new_c = j+dc[k]
                if 0 <= new_r < R and 0 <= new_c < C and graph[new_r][new_c] == "0":
                    exist_boom = True
            if exist_boom == True:
                line += "."
            else:
                line += "0"
        print(line)
elif (N-1) % 4 == 0:
    for i in range(R):
        line = ""
        for j in range(C):
            line += graph[i][j]
        print(line)

