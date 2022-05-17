n = int(input())
count = n ** 2
prefer = {}

for _ in range(count):
    info = list(map(int, input().split()))
    prefer[info[0]] = info[1:]
#print(prefer)

board = [[0 for _ in range(n)] for _ in range(n)]

candidate = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(count)]
#print(candidate)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for pi, preferi in prefer.items():
    #print(pi, preferi)
    candidiate = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                like = 0
                blank = 0
                for di in range(4):
                    nx = i + dx[di] 
                    ny = j + dy[di]
                    if 0<=nx<n and 0<=ny<n:
                        if board[nx][ny] in preferi:
                            like += 1
                        if board[nx][ny] == 0:
                            blank += 1
                candidiate.append([like, blank, i, j])
    #print(candidiate)
    #like 큰것, blank큰것, i, j 작은 것부터
    candidiate.sort(key = lambda x:(-x[0], -x[1], x[2], x[3]))        
    board[candidiate[0][2]][candidiate[0][3]] = pi
    #print(board)
#print(board)

result = 0
for i in range(n):
    for j in range(n):
        like = 0
        for di in range(4):
            nx = i + dx[di] 
            ny = j + dy[di]
            if 0<=nx<n and 0<=ny<n:
                if board[nx][ny] in prefer[board[i][j]]:
                    like += 1
        if like != 0:
            result += 10 ** (like -1)
print(result)

#참고: https://velog.io/@sin5015243/%EB%B0%B1%EC%A4%80-21608-%EC%83%81%EC%96%B4-%EC%B4%88%EB%93%B1%ED%95%99%EA%B5%90-Python
