n = int(input())
m = int(input())

friend = [[]for _ in range(n+1)]
enemy = [[]for _ in range(n+1)]
is_in_team = [False] * (n+1)
for i in range(m):
    ef, p, q = input().split()
    p, q = int(p), int(q)
    if ef == 'E':
        enemy[p].append(q)
        enemy[q].append(p)
    else:
        friend[p].append(q)
        friend[q].append(p)

def dfs(cur):
    is_in_team[cur] = True
    for i in range(len(friend[cur])):
        next = friend[cur][i]
        if is_in_team[next] == False:
            dfs(next) #친구들끼리 dfs
    for i in range(len(enemy[cur])):
        next = enemy[cur][i]
        for j in range(len(enemy[next])):
            nNext = enemy[next][j]
            if is_in_team[nNext] == False:
                dfs(nNext)#원수의 원수는 친구

answer = 0
for i in range(1,n+1):
    if is_in_team[i] == False:
        dfs(i)
        answer += 1
print(answer)

#참고: https://yabmoons.tistory.com/259
