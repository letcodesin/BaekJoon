n = int(input())
m = int(input())
board = [list(map(int, input().split()))for _ in range(n)]
plan = list(map(int, input().split()))

parents = [-1]*(n+1)
for i in range(1, n+1):
    parents[i] = i #자기자신을 부모로 초기화
#print(parents)
def find(a):#a노드의 부모노드 찾음(0일수록 높은 부모)
    if a != parents[a]: #a가 부모노드가 아니면
        parents[a] = find(parents[a])
    return parents[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:#a노드의 부모노드가 더 높은 부모(값이 작을수록 높은 부모)
        parents[b] = a
    else:
        parents[a] = b

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            union(i+1, j+1) #두 도시 집합 결합

#print(parents)
start_parent = parents[plan[0]]
flag = True
for i in range(1, m):
    if parents[plan[i]] != start_parent:
        print("NO")
        flag = False
        break
if flag:
    print("YES")

#참고: https://my-coding-notes.tistory.com/m/332
# https://deep-learning-study.tistory.com/590

