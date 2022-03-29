#백트래킹: 해를 찾는 도중 해가 아니어서 막히면 되돌아가서 다시 해를 찾아가는 기법
def recursive(cur, count, cost):
    global result
    if count == N:
        result = min(result, cost)
        return
    for next in range(N):
        if not visited[next]:
            visited[next] = True
            recursive(next, count + 1, cost + graph[cur][next])
            visited[next] = False

#플로이드와샬 알고리즘 - 모든노드에서 다른 모든 노드까지 최단경로 계산(특정노드를 거쳐가는 경우 사용)
N, K = map(int, input().split())
graph = [[*map(int, input().split())] for _ in range(N)]

# 1. 플로이드 와샬. 모든 정점 최단 거리 구하기
for k in range(N):
    for i in range(N):
        for j in range(N):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

#print(graph)
visited = [False] * N
result = int(1e9)
visited[K] = True

# 2. 행성을 백트래킹으로 탐색하여 모든 행성 방문하여 최소 시간 구하기
recursive(K, 1, 0)
print(result)

#참고: https://ryu-e.tistory.com/42

####################################wrong solution#####################################
#현재 노드에서 한번도 선택되지 않은 path중 무조건 가장 작은 path를 선택->틀린 경우 존재
n, k = map(int, input().split())
adjacent = []
answer = 0
for i in range(n):
    line = []
    temp = list(map(int, input().split()))
    for i in range(len(temp)):
        line.append([temp[i],0])
    adjacent.append(line)
#print(adjacent)
visited = [0 for _ in range(n)]
queue = []
visited[k] = 1
queue.append(k)
while queue:
    cur = queue.pop(0)
    min_path = 1000
    for i in range(len(adjacent[cur])):
        if cur != i and adjacent[cur][i][1] == 0 and min_path > adjacent[cur][i][0]:            
            min_path = adjacent[cur][i][0]
    #print(min_path)
    for i in range(len(adjacent[cur])):
        if min_path == adjacent[cur][i][0]:
            adjacent[cur][i][1] = 1
            queue.append(i)
            answer += adjacent[cur][i][0]
            if visited[i] == 0:
                visited[i] = 1
    if 0 not in visited:
        break
print(answer)
