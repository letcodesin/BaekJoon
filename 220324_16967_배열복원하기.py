H, W, X, Y = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(H+X)]
A = [[0]*W for _ in range(H)]
A_fill = [[0]*W for _ in range(H)]

for i in range(H):
    for j in range(W):
        A_fill[i][j] += 1
        if i+X < H and j+Y < W:
            A_fill[i+X][j+Y] += 1
for i in range(H):
    for j in range(W):
        if A_fill[i][j] == 1:
            A[i][j] = B[i][j]
        elif A_fill[i][j] == 2:
            A[i][j] = B[i][j] - A[i-X][j-Y]
#print(A_fill)
#print(A)

for row in A:
    print(' '.join(map(str, row)))

########################wrong solution###################

H, W, X, Y = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(H+X)]
A = [[0]*W for _ in range(H)]
A_fill = [[False]*W for _ in range(H)]
#print(B)
#print(A)
for i in range(H+X):
    for j in range(W+Y):
        if i < X and j < W:
            A[i][j] = B[i][j]
            A_fill[i][j] = True
        elif i < H and j < Y:
            A[i][j] = B[i][j]
            A_fill[i][j] = True
        elif i >= H:
            A[i-X][j-Y] = B[i][j]
            A_fill[i-X][j-Y] = True

for i in range(H+X):
    for j in range(W+Y):
        if X<=i<H and Y<=j<W:
            if A_fill[i][j] == False and A_fill[i-X][j-Y] == True:
                A[i][j] = B[i][j] - A[i-X][j-Y]
                A_fill[i][j] = True
            elif A_fill[i][j] == True and A_fill[i-X][j-Y] == False:
                A[i-X][j-Y] = B[i][j] - A[i][j]
                A_fill[i-X][j-Y] = True

#print(A)
#print(A_fill)
for row in A:
    print(' '.join(map(str,row)))
