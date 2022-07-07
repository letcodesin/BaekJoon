import sys
input = sys.stdin.readline

n = int(input())
order = []
for _ in range(n):
    t = int(input())
    order.append(list(input().split()))

def move_pivot_side(cube, pivot_index):
    temp1 = cube[pivot_index][0][0]
    temp2 = cube[pivot_index][1][0]
    cube[pivot_index][0][0] = cube[pivot_index][2][0]
    cube[pivot_index][1][0] = cube[pivot_index][2][1]
    cube[pivot_index][2][0] = cube[pivot_index][2][2]
    cube[pivot_index][2][1] = cube[pivot_index][1][2]
    cube[pivot_index][2][2] = cube[pivot_index][0][2]
    cube[pivot_index][1][2] = cube[pivot_index][0][1]
    cube[pivot_index][0][2] = temp1 #cube[pivot_index][0][0]
    cube[pivot_index][0][1] = temp2 #cube[pivot_index][1][0]
    
def move_cube(cube, pivot):
    if pivot == 'U':
        temp = cube[1][0]
        cube[1][0] = cube[4][0] 
        cube[4][0] = cube[5][0] 
        cube[5][0] = cube[3][0] 
        cube[3][0] = temp #cube[1][0]
        move_pivot_side(cube, 0)
    elif pivot == 'D':
        temp = cube[1][2]
        cube[1][2] = cube[3][2] 
        cube[3][2] = cube[5][2] 
        cube[5][2] = cube[4][2] 
        cube[4][2] = temp #cube[1][2]
        move_pivot_side(cube, 2)
    elif pivot == 'F':
        temp = cube[0][2]
        cube[0][2] = [cube[3][2][2], cube[3][1][2], cube[3][0][2]]
        [cube[3][0][2], cube[3][1][2], cube[3][2][2]] = cube[2][0]
        cube[2][0] = [cube[4][2][0], cube[4][1][0], cube[4][0][0]]
        [cube[4][0][0], cube[4][1][0], cube[4][2][0]] = temp #cube[0][2]
        move_pivot_side(cube, 1)
    elif pivot == 'B':
        temp = cube[0][0]
        cube[0][0] = [cube[4][0][2], cube[4][1][2], cube[4][2][2]]
        [cube[4][2][2], cube[4][1][2], cube[4][0][2]] = cube[2][2]
        cube[2][2] = [cube[3][0][0], cube[3][1][0], cube[3][2][0]]
        [cube[3][2][0], cube[3][1][0], cube[3][0][0]] = temp #cube[0][0]
        move_pivot_side(cube, 5)
    elif pivot == 'L':
        temp = [cube[0][0][0], cube[0][1][0], cube[0][2][0]]
        [cube[0][0][0], cube[0][1][0], cube[0][2][0]] = [cube[5][2][2], cube[5][1][2], cube[5][0][2]]
        [cube[5][0][2], cube[5][1][2], cube[5][2][2]] = [cube[2][2][0], cube[2][1][0], cube[2][0][0]]
        [cube[2][0][0], cube[2][1][0], cube[2][2][0]] = [cube[1][0][0], cube[1][1][0], cube[1][2][0]]
        [cube[1][0][0], cube[1][1][0], cube[1][2][0]] = temp
        move_pivot_side(cube, 3)
    elif pivot == 'R':
        temp = [cube[0][0][2], cube[0][1][2], cube[0][2][2]]
        [cube[0][0][2], cube[0][1][2], cube[0][2][2]] = [cube[1][0][2], cube[1][1][2], cube[1][2][2]]
        [cube[1][0][2], cube[1][1][2], cube[1][2][2]] = [cube[2][0][2], cube[2][1][2], cube[2][2][2]]
        [cube[2][0][2], cube[2][1][2], cube[2][2][2]] = [cube[5][2][0], cube[5][1][0], cube[5][0][0]]
        [cube[5][2][0], cube[5][1][0], cube[5][0][0]] = temp
        move_pivot_side(cube, 4)

for i in range(n):
    cube = [[]for _ in range(6)]
    for _ in range(3):
        cube[0].append(['w','w','w'])
        cube[1].append(['r','r','r'])
        cube[2].append(['y','y','y'])
        cube[3].append(['g','g','g'])
        cube[4].append(['b','b','b'])
        cube[5].append(['o','o','o'])

    for j in range(len(order[i])):
        pivot =  order[i][j][0]
        direct =  order[i][j][1]
        if direct == '+':
            count = 1
        else:
            count = 3
        for _ in range(count):
            move_cube(cube, pivot)
    for x in range(3):
        for y in range(3):
            print(cube[0][x][y], end="")
        print()


        