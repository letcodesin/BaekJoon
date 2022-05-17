n, k = map(int, input().split())
belt = list(map(int, input().split()))
robot = [0 for _ in range(n)]
step = 0
while True:
    temp = belt[2*n-1]
    for i in range(2*n-2, -1, -1):
        belt[i+1] = belt[i]
    belt[0] = temp
    temp = robot[n-1]
    for i in range(n-2, -1, -1):
        robot[i+1] = robot[i]
    robot[0] = 0 
    robot[n-1] = 0 #로봇이 내려가는 부분
    #print(belt)
    #print(robot)

    i = n-2
    while i >= 0:
        if robot[i] == 1 and robot[i+1] == 0  and belt[i+1] > 0:
            robot[i+1] = robot[i]
            robot[i] = 0
            belt[i+1] -= 1
        i -= 1
    robot[n-1] = 0 #로봇 내려감

    if robot[0] == 0 and belt[0] > 0:
        robot[0] = 1
        belt[0] -= 1

    step += 1

    if belt.count(0) >= k:
        break

print(step)

#참고: https://jainn.tistory.com/81