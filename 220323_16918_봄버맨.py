import copy

# 입력값을 통해 폭탄의 시간을 가진 배열 채우기
def get_input():
    for i in range(R):
        tmp = str(input())
        for j in range(C):
            if tmp[j] == '.':
                bomb[i][j] = 0  
            else:
                bomb[i][j] = 2
            # 1초 동안 봄버맨은 아무것도 하지 않기 때문에 2를 넣어줌

# 0이면 '.' 1 2 3이면 '0'을 출력
def print_result():
    for i in range(R):
        for j in range(C):
            if bomb[i][j] == 0:
                tmp = '.'  
            else:
                tmp = 'O'
            print(tmp, end="")
        print()

# 비어있는 칸에 새로운 폭탄을 채우고 있는 칸은 1초 시간이 흐르도록 함
def fill_bomb(): 
    for i in range(R):
        for j in range(C):
            if bomb[i][j] == 0:
                bomb[i][j] = 3  
            else:
                bomb[i][j] -= 1

# 0이 된 칸은 주변의 폭탄도 제거
def bomb_explosion(bomb):
    bomb2 = copy.deepcopy(bomb) #bomb2에 값이 변해도 bomb에 값이 변하지 않음
    for i in range(R):
        for j in range(C):
            if bomb[i][j] == 0:
                if 0 <= j-1:
                    bomb2[i][j-1] = 0
                if j+1 < C:
                    bomb2[i][j+1] = 0
                if 0 <= i-1:
                    bomb2[i-1][j] = 0
                if i+1 < R:
                    bomb2[i+1][j] = 0
    return bomb2

R, C, N = map(int, input().split())
bomb = [[0 for _ in range(C)] for _ in range(R)]

if __name__=='__main__':
    get_input()
    for _ in range(N-1):
        fill_bomb()
        bomb = bomb_explosion(bomb)
    print_result()

# 참고: https://dailylifeofdeveloper.tistory.com/195

#######################wrong solution#########################
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

