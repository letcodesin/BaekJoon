from itertools import combinations
from itertools import permutations
n = int(input())
board = []
for _ in range(n):
    line = list(map(int, input().split()))
    board.append(line)
#print(board)

teamnum = n // 2
min_diff = 1e6
for comb in combinations(list(range(n)), teamnum):
    #print(comb)
    start = 0
    for spermut in permutations(comb, 2):
        #print(cpermut)
        start += board[spermut[0]][spermut[1]]
    link = 0
    linkmem = set(range(n)) - set(comb)
    #print(linkmem)
    for lpermut in permutations(list(linkmem), 2):
        link += board[lpermut[0]][lpermut[1]]
    #print(start, link)
    min_diff = min(min_diff, abs(start-link))

print(min_diff)

###############################upgrade solution#########################
#dfs, backtracking
n = int(input())
board = []
for _ in range(n):
    line = list(map(int, input().split()))
    board.append(line)
#print(board)

teamnum = n // 2
min_diff = 1e6
check = [0] * n
def dfs(team_list):
    global min_diff
    if len(team_list) == teamnum:
        #팀 점수 계산
        start = 0
        link = 0
        other_team_list = list(set(range(n)) - set(team_list))
        for i, v in enumerate(team_list):
            for v2 in team_list[i+1:]:
                start += board[v][v2] + board[v2][v]
    
        for i, v in enumerate(other_team_list):
            for v2 in other_team_list[i+1:]:
                link += board[v][v2] + board[v2][v]

        min_diff = min(min_diff, abs(start-link))
        return 
    #팀 설정
    idx = 0
    if len(team_list) > 0:
        idx = team_list[-1]
    for i in range(idx, n):
        if i not in team_list:
            team_list.append(i)
            dfs(team_list)
            team_list.pop()

dfs([])
print(min_diff)

#참고: https://developer-ellen.tistory.com/50?category=879172
#https://velog.io/@sdj4819/%EB%B0%B1%EC%A4%80-14889%EB%B2%88-%EC%8A%A4%ED%83%80%ED%8A%B8%EC%99%80-%EB%A7%81%ED%81%AC-%ED%8C%8C%EC%9D%B4%EC%8D%ACPython
