from copy import deepcopy
n, m, x, y, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
order = list(map(int, input().split()))

dice = [0,0,0,0,0,0,0]

def change_dice(orderi):
    old_dice = deepcopy(dice)
    if orderi == 1:
        dice[1] = old_dice[3]
        dice[3] = old_dice[6]
        dice[4] = old_dice[1]
        dice[6] = old_dice[4]
    elif orderi == 2:
        dice[1] = old_dice[4]
        dice[3] = old_dice[1]
        dice[4] = old_dice[6]
        dice[6] = old_dice[3]
    elif orderi == 3:
        dice[1] = old_dice[2]
        dice[2] = old_dice[6]
        dice[5] = old_dice[1]
        dice[6] = old_dice[5]
    elif orderi == 4:
        dice[1] = old_dice[5]
        dice[2] = old_dice[1]
        dice[5] = old_dice[6]
        dice[6] = old_dice[2]
    #print(dice)

for i in range(k):
    dx, dy = 0, 0
    if order[i] == 1:
        dx, dy = 0, 1
    elif order[i] == 2:
        dx, dy = 0, -1
    elif order[i] == 3:
        dx, dy = -1, 0
    elif order[i] == 4:
        dx, dy = 1, 0
    
    nx = x + dx
    ny = y + dy

    if 0<= nx <n and 0<= ny <m:
        x = nx
        y = ny
        change_dice(order[i])
        if board[x][y] != 0:
            dice[1] = board[x][y]
            board[x][y] = 0
        else:
            board[x][y] = dice[1]
        print(dice[6])
    
    
#참고: https://pacific-ocean.tistory.com/363    
