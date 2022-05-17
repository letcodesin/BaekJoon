from itertools import permutations

n, k = map(int, input().split())
kit = list(map(int, input().split()))

count = 0
for permut in permutations(list(range(n))):
    #print(permut)
    flag = True
    total = 500
    for i in range(n):
        total += -k + kit[permut[i]]
        if total < 500:
            flag = False
            break
    if flag == True:
        count += 1
print(count)

####################other solution_dfs, backtracking###################
n, k = map(int, input().split())
kit = list(map(int, input().split()))

check = [0] * n
count = 0

def dfs(depth, total):
    global count
    if depth == n:
        count += 1
        return
    for i in range(n):
        if check[i] == 1 or total + kit[i] -k < 500:
            continue
        check[i] = 1
        dfs(depth+1, total+kit[i]-k)
        check[i] = 0

dfs(0,500)
print(count)

#참고: https://jinho-study.tistory.com/1040
# https://thyong.tistory.com/2