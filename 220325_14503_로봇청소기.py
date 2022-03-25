n, m = map(int, input().split())
r, c, d = map(int, input().split())
graph = [list(map(int, input().split()))for _ in range(n)]
#print(graph)

# 방향bang = 0->3/1->0/2->1/3->2 => (bang+3)%4가 다음 방향
# 0->3->2->1 순서대로 돌아야함
# bang=0일때->다음bang=3이되고 북쪽 방향의 왼쪽으로 가야하니 r, c-1 => dr[3]=0, dc[3]=-1
# bang=3일때->다음bang=2이되고 서쪽 방향의 왼쪽으로 가야하니 r+1, c => dr[2]=1, dc[2]=0
# bang=2일때->다음bang=1이되고 남쪽 방향의 왼쪽으로 가야하니 r, c+1 => dr[1]=0, dc[1]=1
# bang=1일때->다음bang=0이되고 동쪽 방향의 왼쪽으로 가야하니 r-1, c => dr[0]=-1, dc[2]=0
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
 
count = 1
x, y = r, c
graph[x][y] = 2 # 방문처리를 2로 함
 
while True:
    check = False # 방문한 칸이 있는지 없는지 유뮤를 판단하기 위한 bool형 변수 check
    for i in range(4): # 4방향을 돌며
        d = (d+3)%4
        nx = x + dr[d]
        ny = y + dc[d]
        if 0 <= nx < n and 0 <= ny < m: 
            if graph[nx][ny] == 0: 
                count += 1
                graph[nx][ny] = 2 #청소함
                x, y = nx, ny
                check = True 
                break
    if not check: #회전하며 4방향 다 탐색했는데 청소할 공간이 없는 경우 후진
        nx = x - dr[d]#bang=0일때 모든 방향 다 본 다음 다시 bang=0->뒤로 후진
        ny = y - dc[d]
        if 0 <= nx < n and 0 <= ny < m: # nx, ny가 그래프를 벗어나지 않는지 확인
            if graph[nx][ny] == 2: #이미 청소한 칸인경우 후진
                x, y = nx, ny
            elif graph[nx][ny] == 1: #벽인 경우 
                print(count)
                break
        else:
            print(count)
            break

#참고: https://bgspro.tistory.com/64
# https://resilient-923.tistory.com/164