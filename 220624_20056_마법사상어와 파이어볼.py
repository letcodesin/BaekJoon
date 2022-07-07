n, m, k = map(int, input().split())
fire_ball = []
for _ in range(m):
    line = list(map(int, input().split()))
    fire_ball.append(line)

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

board = [[[] for _ in range(n)] for _ in range(n)]

for i in range(m):
    board[fire_ball[i][0]-1][fire_ball[i][1]-1].append(fire_ball[i][2:])
#print(board)

for _ in range(k):
    new_board =  [[[] for _ in range(n)] for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if len(board[x][y]) > 0:
                for z in range(len(board[x][y])):
                    nx = x + dx[board[x][y][z][2]]*board[x][y][z][1]
                    ny = y + dy[board[x][y][z][2]]*board[x][y][z][1]
                    nx = nx % n
                    ny = ny % n
                    new_board[nx][ny].append(board[x][y][z])
    #print(new_board)
    board = new_board
    for x in range(n):
        for y in range(n):
            if len(board[x][y]) > 1:
                weight_sum = 0
                speed_sum = 0
                all_even = True
                all_odd = True
                for z in range(len(board[x][y])):
                    weight_sum += board[x][y][z][0]
                    speed_sum += board[x][y][z][1]
                    if board[x][y][z][2] % 2 == 1:
                        all_even = False
                    else:
                        all_odd = False
                new_weight = weight_sum // 5
                new_speed = speed_sum // len(board[x][y])
                all_direct = []
                if all_even or all_odd:
                    all_direct = [0, 2, 4, 6]
                else:
                    all_direct = [1, 3, 5, 7]
                board[x][y] = []
                if new_weight > 0:
                    for z in range(4):
                        board[x][y].append([new_weight, new_speed, all_direct[z]])
    #print(board)

fire_ball_sum = 0
for x in range(n):
    for y in range(n):
        if len(board[x][y]) > 0:
            for z in range(len(board[x][y])):
                fire_ball_sum += board[x][y][z][0]
print(fire_ball_sum)

###########################other solution###########################
#fireball list를 이용한 풀이
N, M, K = map(int, input().split())
fireballs = []
for _ in range(M):
    _r, _c, _m, _s, _d = list(map(int, input().split()))
    fireballs.append([_r-1, _c-1, _m, _s, _d])

MAP = [[[] for _ in range(N)] for _ in range(N)]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(K):
    # 파이어볼 이동
    while fireballs:
        cr, cc, cm, cs, cd = fireballs.pop(0)
        nr = (cr + cs * dx[cd]) % N  # 1번-N번 행 연결되어있기 때문
        nc = (cc + cs * dy[cd]) % N
        MAP[nr][nc].append([cm, cs, cd])

    # 2개 이상인지 체크
    for r in range(N):
        for c in range(N):
            # 2개 이상인 경우 -> 4개의 파이어볼로 쪼개기
            if len(MAP[r][c]) > 1:
                sum_m, sum_s, cnt_odd, cnt_even, cnt = 0, 0, 0, 0, len(MAP[r][c])
                while MAP[r][c]:
                    _m, _s, _d = MAP[r][c].pop(0)
                    sum_m += _m
                    sum_s += _s
                    if _d % 2:
                        cnt_odd += 1
                    else:
                        cnt_even += 1
                if cnt_odd == cnt or cnt_even == cnt:  # 모두 홀수이거나 모두 짝수인 경우
                    nd = [0, 2, 4, 6]
                else:
                    nd = [1, 3, 5, 7]
                if sum_m//5:  # 질량 0이면 소멸
                    for d in nd:
                        fireballs.append([r, c, sum_m//5, sum_s//cnt, d])

            # 1개인 경우
            if len(MAP[r][c]) == 1:
                fireballs.append([r, c] + MAP[r][c].pop())

print(sum([f[2] for f in fireballs]))