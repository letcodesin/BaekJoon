from itertools import combinations

n, m = map(int,input().split())
home = []
chicken = []
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(n):
        if line[j] == 1:
            home.append((i, j))
        elif line[j] == 2:
            chicken.append((i, j))

#print(home)
#print(chicken)

answer = 10000
for comb in combinations(range(len(chicken)),m):
    surv_chicken = []
    for idx in comb:
        surv_chicken.append(chicken[idx])
    #print(surv_chicken)
    chicken_len = 0
    for i in range(len(home)):
        path = 10000
        for j in range(len(surv_chicken)):
            cur_path = abs(home[i][0] - surv_chicken[j][0]) + abs(home[i][1] - surv_chicken[j][1])
            path = min(path, cur_path)
        chicken_len += path
    #print(chicken_len)
    answer = min(answer, chicken_len)
print(answer)
