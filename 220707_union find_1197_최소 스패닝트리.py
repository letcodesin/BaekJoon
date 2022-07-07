import sys
input = sys.stdin.readline
v, e = map(int, input().split())
edge = []
for _ in range(e):
    v1, v2, weight = map(int, input().split())
    edge.append((v1, v2, weight))

edge.sort(key = lambda x: (x[2]))
#print(edge)

parent = list(range(v+1))
#print(parent)
def find(v):
    if v != parent[v]:
        parent[v] = find(parent[v])
    return parent[v]

def union(v1, v2):
    v1 = find(v1)
    v2 = find(v2)
    if v1 < v2:
        parent[v2] = v1
    else:
        parent[v1] = v2

total_weight = 0
for i in range(len(edge)):
    v1, v2, weight = edge[i]
    if find(v1) != find(v2):
        union(v1, v2)
        #print(parent)
        total_weight+= weight
print(total_weight)

#참고: https://velog.io/@coding_egg/%EB%B0%B1%EC%A4%80-1197%EB%B2%88-%EC%B5%9C%EC%86%8C-%EC%8A%A4%ED%8C%A8%EB%8B%9D-%ED%8A%B8%EB%A6%AC-python-%ED%8C%8C%EC%9D%B4%EC%8D%AC
