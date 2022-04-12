n = int(input())
board = list(map(int, input().split()))
tree = [[]for _ in range(n)]

for me, parent in enumerate(board):
    if parent != -1:
        tree[parent].append(me)
#dp[i]: i를 루트로하는 서브트리에 소식을 전달하는데 걸리는 최대 시간
dp = [0 for _ in range(n)] 
def dfs(me):
    childeren = []
    for child in tree[me]:
        dfs(child)
        childeren.append(dp[child])
    if childeren:
        childeren.sort(reverse = True)
        next_time = []
        for i in range(len(childeren)):
            next_time.append(childeren[i] + i + 1)
        dp[me] = max(next_time)

dfs(0)
print(dp[0])

#참고: https://cocook.tistory.com/151
