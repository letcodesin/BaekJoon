from collections import deque

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

def bfs(r1,c1):
    queue = deque()
    queue.append((r1,c1))
    cow_visited_map[r1][c1] = True
    while queue:
        r2, c2 = queue.popleft()
        for i in range(4):
            new_r2 = r2 + dr[i]
            new_c2 = c2 + dc[i]
            if new_r2<0 or new_c2<0 or new_r2>=N or new_c2>=N:
                continue
            if cow_visited_map[new_r2][new_c2] == True:
                continue
            if (new_r2, new_c2) in road[r2][c2]:
                continue
            queue.append((new_r2, new_c2))
            cow_visited_map[new_r2][new_c2] = True


N, K, R = map(int, input().split())
road = [[[]for _ in range(N)]for _ in range(N)]
cow_list = []
#print(road)

for i in range(R):
    r1, c1, r2, c2 = map(int, input().split())
    road[r1-1][c1-1].append((r2-1,c2-1))
    road[r2-1][c2-1].append((r1-1,c1-1))
#print(road)

for i in range(K):
    r1, c1 = map(int, input().split())
    cow_list.append((r1-1, c1-1))
#print(cow_list)

unvisited_count = 0
for i in range(K):
    cow_visited_map = [[False]*N for _ in range(N)]
    bfs(cow_list[i][0], cow_list[i][1])
    for j in range(i+1, K):
        if cow_visited_map[cow_list[j][0]][cow_list[j][1]] == False:
            unvisited_count += 1
        
print(unvisited_count)



#참고: https://skygood95.tistory.com/38
# https://ryu-e.tistory.com/36
