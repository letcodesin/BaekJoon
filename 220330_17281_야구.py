from itertools import permutations

n = int(input())
board = [list(map(int, input().split()))for _ in range(n)]

#1. 순열을 통해 타순을 구합니다.(타순은 이닝이 바뀌어도 그대로 유지됨)
#2. 해당 타순으로 N 이닝을 수행한 점수를 구합니다.
#3. 위 과정을 가능한 모든 타순에 대해 수행하고 최대 점수를 출력합니다.

people = [1, 2, 3, 4, 5, 6, 7, 8] #0번선수는 무조건 4번타자(3번째)
answer = 0
for permute in permutations(people, 8):
    #print(permute)
    permute = list(permute)
    order = permute[:3] + [0] + permute[3:] #0번선수는 무조건 4번타자(3번째)
    #print(order)
    score = 0
    member_idx = 0
    for inning in range(n):
        outcount = 0
        base1, base2, base3 = 0, 0, 0
        while outcount != 3:
            if board[inning][order[member_idx]] == 0:
                outcount += 1
            elif board[inning][order[member_idx]] == 1:
                score += base3
                base1, base2, base3 = 1, base1, base2
            elif board[inning][order[member_idx]] == 2:
                score += (base2 + base3)
                base1, base2, base3 = 0, 1, base1
            elif board[inning][order[member_idx]] == 3:
                score += (base1 + base2 + base3)
                base1, base2, base3 = 0, 0, 1
            elif board[inning][order[member_idx]] == 4:
                score += (base1 + base2 + base3 + 1)
                base1, base2, base3 = 0, 0, 0
            member_idx += 1
            if member_idx == 9:
                member_idx = 0

    answer = max(answer, score)
print(answer)
            

#참고: https://jjangsungwon.tistory.com/75
#https://bladejun.tistory.com/113