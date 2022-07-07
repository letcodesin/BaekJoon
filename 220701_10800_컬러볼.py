import sys
input = sys.stdin.readline #시간단축시 필요

n = int(input())
ball = []
for i in range(n):
    color, size = map(int, input().split())
    ball.append([i, color, size])
ball.sort(key = lambda x: (x[2], x[1]))
#print(ball)
color_sum = [0] * 200001
ball_sum = [0] * n

tsum = 0
i = 0
j = 0
while i < n:
    while ball[i][2] > ball[j][2]:
        tsum += ball[j][2]
        color_sum[ball[j][1]] += ball[j][2]
        j += 1
    ball_sum[ball[i][0]] = tsum - color_sum[ball[i][1]]
    i += 1
result = []
for i in range(n):
    result.append(str(ball_sum[i]))
print('\n'.join(result))

###################시간초과 풀이###################
'''
n = int(input())
ball = []
for _ in range(n):
    ball.append(list(map(int, input().split())))

for i in range(n):
    sum = 0
    for j in range(n):
        if ball[i][0] != ball[j][0] and ball[i][1] > ball[j][1]:
            sum += ball[j][1]
    print(sum)
'''
