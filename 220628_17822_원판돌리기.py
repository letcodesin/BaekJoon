from collections import deque
n, m, t = map(int, input().split())
circle = []
info = []
for _ in range(n):
    circle.append(deque(map(int, input().split())))
for _ in range(t):
    info.append(list(map(int, input().split())))

for ti in range(t):
    cnum, direct, time = info[ti]
    tsum = 0
    for i in range(n):
        tsum += sum(circle[i])
        if (i+1) % cnum == 0:
            
            if direct == 0:
                circle[i].rotate(time)
            else:
                circle[i].rotate(-time)
            '''
            #틀린 코드
            if direct == 1:
                time = -time
            circle[i].rotate(time)
            '''
    #print(circle)
    if tsum != 0:
        #인접한 수 지우기
        remove_index = []
        for i in range(n):
            for j in range(m-1):
                if circle[i][j] != 0 and circle[i][j+1] != 0 and circle[i][j] == circle[i][j+1]:
                    remove_index.append((i,j))
                    remove_index.append((i,j+1))
            if circle[i][0] != 0 and circle[i][-1] != 0 and circle[i][0] == circle[i][-1]:
                remove_index.append((i,0))
                remove_index.append((i,m-1))
        for j in range(m):
            for i in range(n-1):
                if circle[i][j] != 0 and circle[i+1][j]!= 0 and circle [i][j] == circle[i+1][j]:
                    remove_index.append((i,j))
                    remove_index.append((i+1,j))
        remove_index = list(set(remove_index))

        for i in range(len(remove_index)):
            x, y = remove_index[i]
            circle[x][y] = 0

        #print(circle)
        if len(remove_index) == 0:
            total_sum = 0
            zero_count = 0
            for i in range(n):
                total_sum += sum(circle[i])
                zero_count += circle[i].count(0)
            mean_num = total_sum / (m*n - zero_count)
            #print(mean_num)
            for i in range(n):
                for j in range(m):
                    if circle[i][j] != 0 and circle[i][j] > mean_num:
                            circle[i][j] -= 1
                    elif circle[i][j] != 0  and circle[i][j] < mean_num:
                            circle[i][j] += 1
    else:
        break
total_sum = 0
for i in range(n):
    total_sum += sum(circle[i])
print(total_sum)
# 참고: https://hoyeonkim795.github.io/posts/17822/
'''
###################틀린 풀이######################
from collections import deque
n, m, t = map(int, input().split())
circle = []
for _ in range(n):
    circle.append(deque(map(int, input().split())))
order = []
for _ in range(t):
    cnum, direct, time = map(int, input().split())
    delete_num = False
    cindex = []
    for i in range(1, n+1):
        if i % cnum == 0:
            cindex.append(i-1)
    print(cindex)
    while cindex:
        if direct == 1:
            time = -1 * time
        circle[cindex[0]].rotate(time)
        cindex.pop(0)
    print(circle)
    #인접한 수 지우기
    for i in range(n-1):
        for j in range(m):
            #마지막 수랑 첫번째 수랑 인접함
            if j == m-1:
                if circle[i][j] != 0 and circle[i][j] == circle[i][0]:
                    circle[i][0] = 0
                    circle[i][j] = 0
                    delete_num = True
                if circle[i][j] != 0 and circle [i][j] == circle[i+1][j]:
                    circle[i+1][j] = 0
                    circle[i][j] = 0
                    delete_num = True
            else:
                if circle[i][j] != 0 and circle[i][j] == circle[i][j+1]:
                    circle[i][j+1] = 0
                    circle[i][j] = 0
                    delete_num = True
                if circle[i][j] != 0 and circle [i][j] == circle[i+1][j]:
                    circle[i+1][j] = 0
                    circle[i][j] = 0
                    delete_num = True
    for j in range(m):
        if j == m-1:
            if circle[n-1][j] != 0 and circle[n-1][j] == circle[n-1][0]:
                circle[n-1][0] = 0
                circle[n-1][j] = 0
                delete_num = True
        else:
            if circle[n-1][j] != 0 and circle[n-1][j] == circle[n-1][j+1]:
                circle[n-1][j+1] = 0
                circle[n-1][j] = 0
                delete_num = True
    print(circle)
    if delete_num == False:
        print("False")
        total_sum = 0
        zero_count = 0
        for i in range(n):
            total_sum += sum(circle[i])
            zero_count += circle[i].count(0)
        mean_num = total_sum / (m*n - zero_count)
        print(mean_num)
        for i in range(n):
            for j in range(m):
                if circle[i][j] != 0:
                    if circle[i][j] < mean_num:
                        circle[i][j] += 1
                    elif circle[i][j] > mean_num:
                        circle[i][j] -= 1
        print(circle)
total_sum = 0
for i in range(n):
    total_sum += sum(circle[i])
print(total_sum)
'''