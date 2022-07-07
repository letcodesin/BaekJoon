import sys
input = sys.stdin.readline
n = int(input())
edge = []
for _ in range(n):
    edge.append(tuple(map(int, input().split())))

edge.sort()
sum = 0
left = edge[0][0]
right = edge[0][1]
for i in range(1, n):
    if right >= edge[i][1]:
        continue
    elif edge[i][0] <= right < edge[i][1]:
        right = edge[i][1]
    elif right < edge[i][0]:
        sum += right - left
        left = edge[i][0]
        right = edge[i][1]
sum += right - left
print(sum)

'''
#################################시간초과 풀이#################################
n = int(input())
edge = []
for _ in range(n):
    edge.append(tuple(map(int, input().split())))

edge.sort(key = lambda x: x[0])
sum = 0
left = edge[0][0]
right = edge[0][1]
for i in range(n):
    if edge[i][0] < right:
        right = max(edge[i][1], right)
    else:
        #print(left, right)
        sum += right - left
        left = edge[i][0]
        right = edge[i][1]
    
sum += right - left
print(sum)
#################################시간초과 풀이#################################
from copy import deepcopy

n = int(input())
edge = []
for _ in range(n):
    edge.append(list(map(int, input().split())))

edge.sort(key = lambda x:(x[0], x[1]))

new_line = deepcopy(edge)
pop_index = []
for i in range(n-1):
    if edge[i+1][0] < edge[i][1]:
        new_line[i+1][0] = min(new_line[i][0], new_line[i+1][0])
        new_line[i][1] = max(new_line[i+1][1], new_line[i][1])
#print(new_line)

sum = 0
i = 0
while i < n-1:
    if new_line[i+1][0] == new_line[i][0] and new_line[i+1][1] == new_line[i][1]:
        i+=1
    else:
        #print(i)
        sum += new_line[i][1] - new_line[i][0]
        i+= 1
if new_line[n-2][0] != new_line[n-1][0] or new_line[n-2][1] != new_line[n-1][1]:
    sum += new_line[n-1][1] - new_line[n-1][0]
print(sum)
'''
