def solution(adjacent_list, k, v):
    answer = 0
    queue = []
    visited = [-1] * N
    queue.append(v)
    visited[v] = 1
    while queue:
        current_node = queue.pop(0)
        for next_node, next_k in adjacent_list[current_node]:
            if next_k >= k and visited[next_node] == -1:
                queue.append(next_node)
                visited[next_node] = 1
                answer += 1
    return answer

N, Q = map(int, input().split())
adjacent_list = [[] for _ in range(N)]
for i in range(N - 1):
    p, q, r = map(int, input().split())
    adjacent_list[p-1].append([q-1, r])
    adjacent_list[q-1].append([p-1, r])
#print(adjacent_list)
k_list = []
v_list = []
for i in range(Q):
    k, v = map(int, input().split())
    k_list.append(k)
    v_list.append(v)
for i in range(len(k_list)):
    print(solution(adjacent_list, k_list[i], v_list[i]-1))
