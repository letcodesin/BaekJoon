from collections import deque

def check_right(topnum, direct):
    if topnum > 4 or topnie[topnum-1][2] == topnie[topnum][6]:
        return
    if topnie[topnum-1][2] != topnie[topnum][6]:
        check_right(topnum+1, -direct)
        topnie[topnum].rotate(direct)

def check_left(topnum, direct):
    if topnum < 1 or topnie[topnum][2] == topnie[topnum+1][6]:
        return
    if topnie[topnum][2] != topnie[topnum+1][6]:
        check_left(topnum-1, -direct)
        topnie[topnum].rotate(direct)

topnie = {}
for i in range(1, 5):
    topnie[i] = deque(list(map(int, input())))
#print(topnie)
k = int(input())
for _ in range(k):
    topnum, direct = map(int, input().split())
    check_right(topnum+1, -direct)
    check_left(topnum-1, -direct)
    topnie[topnum].rotate(direct)

result = 0
for i in range(4):
    result += 2**i * topnie[i+1][0]
print(result)

#참고: https://inspirit941.tistory.com/entry/Python-%EB%B0%B1%EC%A4%80-14891-%ED%86%B1%EB%8B%88%EB%B0%94%ED%80%B4
