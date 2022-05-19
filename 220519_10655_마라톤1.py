########################시간초과#########################
n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
#print(board)
total = 1e7
for out in range(1,n-1):
    dist = 0
    flag = False
    for i in range(1, n):
        if flag == False:
            cur_x = board[i-1][0]
            cur_y = board[i-1][1]
        else:
            flag = False
        if i == out:
            flag = True
            continue
        dist += abs(board[i][0]-cur_x) + abs(board[i][1]-cur_y)
    #print(dist)
    total = min(total, dist)
print(total)

############################upgrade solution############################
n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
#print(board)
max_diff = 0
for i in range(1,n-1):
    origin_dist = abs(board[i][0]-board[i-1][0]) + abs(board[i][1]-board[i-1][1]) + abs(board[i+1][0]-board[i][0]) + abs(board[i+1][1]-board[i][1])
    skip_dist = abs(board[i+1][0]-board[i-1][0]) + abs(board[i+1][1]-board[i-1][1])
    max_diff = max(max_diff, abs(origin_dist-skip_dist))

total_dist = 0
for i in range(1, n):
    cur_x = board[i-1][0]
    cur_y = board[i-1][1]
    total_dist += abs(board[i][0]-cur_x) + abs(board[i][1]-cur_y)    
print(total_dist - max_diff)

#참고: https://acupoframen.tistory.com/12