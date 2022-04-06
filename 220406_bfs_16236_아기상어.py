#먹을 수 있는 물고기를 bfs로 전체 board를 순회하며 찾음
from collections import deque
n = int(input())
board = [list(map(int, input().split()))for _ in range(n)]
answer = 0
baby_size = 2
fish_cnt = 0
fish_pos = []
eat = []
for i in range(n):
    for j in range(n):
        if 0 < board[i][j] <=6:
            fish_cnt +=1
            fish_pos.append((i,j))
        elif board[i][j] == 9:
            baby_pos = [i, j]
board[baby_pos[0]][baby_pos[1]]=0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(baby_pos):
    queue = deque([(0, baby_pos[0], baby_pos[1])])
    eat = []
    visited = [[False]*n for _ in range(n)]
    visited[baby_pos[0]][baby_pos[1]] = True
    #min_fish_dist = 1000000
    while queue:
        eatten = queue.popleft()
        for i in range(4):
            nx = eatten[1] + dx[i]
            ny = eatten[2] + dy[i]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny] == False:
                if board[nx][ny] <= baby_size:
                    visited[nx][ny] = True
                    if 0 < board[nx][ny] < baby_size:
                        eat.append((eatten[0]+1, nx, ny))
                        #min_fish_dist = eatten[0]+1
                    #if eatten[0]+1 <= min_fish_dist:
                    queue.append((eatten[0]+1, nx, ny))
    if len(eat) > 0:
        eat.sort()
        return eat[0]
    else:
        return False

answer = 0
eat_count = 0
while fish_cnt :
    min_fish = bfs(baby_pos)
    if not min_fish:
        break
    baby_pos = [min_fish[1],min_fish[2]]
    answer +=min_fish[0]
    eat_count+=1
    fish_cnt-=1
    if baby_size == eat_count:
        baby_size +=1
        eat_count =0
    board[baby_pos[0]][baby_pos[1]] = 0
print(answer)

#참고: https://11001.tistory.com/96

###########################wrong solution#######################
#반례: 먹을 물고기까지 길에 baby_size보다 큰 물고기가 있어 돌아가야 하는 경우
#먹을 물고기까지 길이 abs(i - baby_pos[0]) + abs(j - baby_pos[1]) 가 아닌 경우
# 0 0 0 1
# 0 0 0 2
# 0 2 0 0 
# 3 9 3 1
n = int(input())
board = [list(map(int, input().split()))for _ in range(n)]
#print(board)
answer = 0
baby_size = 2
eat = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 9:
            baby_pos = [i, j]
#print(baby_pos)
for i in range(n):
    for j in range(n):        
        if board[i][j] != 0 and baby_size > board[i][j]:
            eat.append([abs(i - baby_pos[0]) + abs(j - baby_pos[1]), i, j])
eat.sort()
#print(eat)

eat_count = 0
while len(eat) > 0:
    eatten = eat.pop(0)
    answer += eatten[0]
    board[eatten[1]][eatten[2]] = 0
    baby_pos = [eatten[1], eatten[2]]
    eat_count += 1
    #print(answer, eat_count, baby_pos)
    if eat_count == baby_size:
        baby_size += 1
        eat_count = 0
    eat=[]
    for i in range(n):
        for j in range(n):        
            if board[i][j] != 0 and baby_size > board[i][j]:
                 eat.append([abs(i - baby_pos[0]) + abs(j - baby_pos[1]), i, j])
    eat.sort()
print(answer)