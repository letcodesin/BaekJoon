import sys
input = sys.stdin.readline

a, b = map(int, input().split())
n, m = map(int, input().split())
board = [[0 for _ in range(a)]for _ in range(b)]
position = []
order = []
for i in range(n):
    x, y, direct = input().split()
    idirect = -1
    if direct =='N':
        idirect = 0
    elif direct =='E':
        idirect = 1
    elif direct =='S':
        idirect = 2
    elif direct =='W':
        idirect = 3
    r = b-int(y)
    c = int(x)-1
    position.append([r, c, idirect])
    board[r][c] = i+1
#print(board)
for _ in range(m):
    order.append(input().split())

#NESW
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(m):
    robot, cur_order, turn = order[i]
    cur_robot = int(robot)
    turn = int(turn)
    row, col, direct = position[cur_robot-1]
    if cur_order == 'R':
        direct = (direct + turn) % 4
        position[cur_robot-1] = [row, col, direct]
    elif cur_order == 'L':
        for _ in range(turn):
            direct -= 1
            if direct == -1:
                direct = 3
        position[cur_robot-1] = [row, col, direct]
    else:
        for _ in range(turn):
            if 0<= row + dx[direct] < b and 0<= col + dy[direct] < a:
                if board[row + dx[direct]][col + dy[direct]]  != 0:
                    print("Robot "+str(cur_robot)+" crashes into robot "+str(board[row + dx[direct]][col + dy[direct]]))
                    sys.exit(0)
                board[row][col] = 0
                row = row + dx[direct]
                col = col + dy[direct]
                board[row][col] = cur_robot
                position[cur_robot-1] = [row, col, direct]
                #print(position[cur_robot-1])
                #print(board)
            else:
                print("Robot "+str(cur_robot)+" crashes into the wall")
                sys.exit(0)
print("OK")