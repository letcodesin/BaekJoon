from copy import deepcopy

n, m = map(int, input().split())
t = list(map(int, input().split()))
old_truth = set()
truth = set()
mparty = []
if t[0] > 0:
    truth.update(t[1:])
    #print(truth)
    old_truth = deepcopy(truth)
for _ in range(m):
    party = list(map(int, input().split()))
    mparty.append(party[1:])
    for tr in truth:
        if tr in party[1:]:
            truth.update(party[1:])
            break
while len(old_truth) != len(truth):
    old_truth = deepcopy(truth)
    for i in range(m):    
        for tr in truth:
            if tr in mparty[i]:
                truth.update(mparty[i])
                break
#print(truth)
#print(mparty)
if t[0] == 0:
    print(m)
else:
    count = 0
    for i in range(m):
        flag = False
        for tr in truth:
            if tr in mparty[i]:
                flag = True
                break
        if flag == False:
            count += 1
    print(count)

##########################upgrade solution#######################
def find(parent, p):
    if p != parent[p]:
        parent[p] = find(parent, parent[p])
    return parent[p]

def union(parent, p1, p2, truth):
    p1 = find(parent, p1)
    p2 = find(parent, p2)
    if p1 in truth and p2 in truth:
        return
    if p1 in truth:
        parent[p2] = p1
    elif p2 in truth:
        parent[p1] = p2
    else:
        if p1 < p2:
            parent[p2] = p1
        else:
            parent[p1] = p2

n, m = map(int, input().split())
truth = list(map(int, input().split()))[1:]
mparty = []
parent = list(range(n+1))
for _ in range(m):
    party_info = list(map(int, input().split()))
    party_len = party_info[0]
    party = party_info[1:]
    mparty.append(party)
    
    for i in range(party_len-1):
        union(parent, party[i], party[i+1], truth)

count = 0
for i in range(m):
    for j in range(len(mparty[i])):
        if find(parent, mparty[i][j]) in truth:
            break
    else:
        count += 1

print(count)

#참고: https://seongonion.tistory.com/131

'''
추가 예제
10 10
4 1 2 3 4
2 1 5
2 2 6
1 7
1 8
2 7 8
2 1 7
1 9
1 10
2 3 10
1 4

결과: 1

truth의 변화
1 2 3 4
1 2 3 4 5 6 7 10
1 2 3 4 5 6 7 8 10
'''