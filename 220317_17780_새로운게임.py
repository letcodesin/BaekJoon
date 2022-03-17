import sys
dh = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
def move(mal_index):
    old_hang = mal[mal_index][0]
    old_yal = mal[mal_index][1]
    old_bang = mal[mal_index][2]
    if mal_index != chess_map[old_hang][old_yal][0]:#맨 밑의 말이 아니면
        return 0
    new_hang = old_hang + dh[mal[mal_index][2]]
    new_yal = old_yal + dy[mal[mal_index][2]]

    if new_hang >= N or 0 > new_hang or new_yal >= N or 0 > new_yal or pan[new_hang][new_yal] == 2:
        if old_bang == 0:
            new_bang = 1
        elif old_bang == 1:
            new_bang = 0
        elif old_bang == 2:
            new_bang = 3
        else:
            new_bang = 2
        mal[mal_index][2] = new_bang
        new_hang = old_hang + dh[new_bang]
        new_yal = old_yal + dy[new_bang]
        if new_hang >= N or 0 > new_hang or new_yal >= N or 0 > new_yal or pan[new_hang][new_yal] == 2:
            return 0 #방향만 바꿈

    chess_list = chess_map[old_hang][old_yal]
    chess_map[old_hang][old_yal] = []
    if pan[new_hang][new_yal] == 1:
        chess_list = chess_list[::-1]
    for i in chess_list:
        chess_map[new_hang][new_yal].append(i)
        mal[i][:2] = [new_hang, new_yal]
    if len(chess_map[new_hang][new_yal]) >= 4:
        return 1
    return 0
N, K = map(int, input().split())
pan = []
for i in range(N):
    pan.append(list(map(int, input().split())))
#print(pan)

mal = []
chess_map = [[[]for i in range(N)]for j in range(N)]
for i in range(K):
    h, y, bang = map(int, input().split())
    mal.append([h-1, y-1, bang-1])
    chess_map[h-1][y-1].append(i)
#print(mal)
#print(chess_map)

turn = 1
while turn <= 1000:
    for i in range(K):
        flag = move(i)
        if flag == 1:
            print(turn)
            sys.exit() 
    turn += 1
print(-1)