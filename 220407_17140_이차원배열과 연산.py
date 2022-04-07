r, c, k = map(int, input().split())
A = [list(map(int, input().split()))for _ in range(3)]
#print(A)
answer = 0

def R_sort(A):
    B = []
    count = 0
    for i in range(len(A)):
        line = dict()
        for j in range(len(A[i])):
            if A[i][j] == 0:
                continue
            if A[i][j] not in line:
                line[A[i][j]] = 1
            else:
                line[A[i][j]] += 1
        line = sorted(line.items(), key = lambda x: (x[1], x[0]))
        if len(line) >= 100:
            line = line[:100]
        temp = []
        for li in line:
            temp.append(li[0])
            temp.append(li[1])
        count = max(count, len(temp))
        B.append(temp)
    for i in range(len(B)):
        while len(B[i]) != count:
            B[i].append(0)
    return B


while answer <= 100:
    if len(A) >= r and len(A[0]) >= c:
        if A[r-1][c-1] == k:
            break
    if len(A) >= len(A[0]):
        #R연산
        A = R_sort(A)
    else:
        #C연산
        A = list(map(list,zip(*A)))#A행렬의 Transpose: 열을 행으로 바꿔 R_sort계산 
        A = R_sort(A)
        A = list(map(list,zip(*A)))
    answer += 1
if answer == 101:
    answer = -1
print(answer)

# 참고: https://velog.io/@wook2pp/%EB%B0%B1%EC%A4%80-17140-%EC%9D%B4%EC%B0%A8%EC%9B%90-%EB%B0%B0%EC%97%B4%EA%B3%BC-%EC%97%B0%EC%82%B0
