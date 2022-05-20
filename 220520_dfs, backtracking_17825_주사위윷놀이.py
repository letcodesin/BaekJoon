graph = [[1], [2], [3], [4], [5], [6, 21], [7], [8], [9], [10], [11, 25], [12], [13], [14], [15], [16, 27], [17], [18], [19], [20], [32], [22], [23], [24], [30], [26], [24], [28], [29], [24], [31], [20], [32]] 
score = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 13, 16, 19, 25, 22, 24, 28, 27, 26, 30, 35, 0]
dice_num = list(map(int, input().split()))

answer = 0
def dfs(idx, result, horse):
    global answer
    if idx >= 10:
        answer = max(answer, result)
        return
    for i in range(4):
        loci = horse[i] #i번째 horse의 위치
        if len(graph[loci]) == 2:
            loci = graph[loci][1]
        else:
            loci = graph[loci][0]
        for _ in range(1, dice_num[idx]):#dice_num 횟수만큼 horse 위치 이동
            loci = graph[loci][0]
        if loci == 32 or (loci < 32 and loci not in horse):#다른 말을 움직일 수 있는 조건이면
            before_loci = horse[i]#i번째 horse의 이동 이전 위치
            horse[i] = loci#i번째 horse가 이동한 후 위치
            dfs(idx+1, result + score[loci], horse)#현상태에서 다음 주사위 숫자만큼 horse 이동
            horse[i] = before_loci

dfs(0, 0, [0,0,0,0])
print(answer)

#참고: https://juhi.tistory.com/52