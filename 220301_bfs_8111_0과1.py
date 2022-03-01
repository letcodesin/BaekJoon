remain_visited =[['',0] for _ in range(20001)] #나머지 값 배열
#배열 첫번째 값은 해당 나머지를 갖는 0과 1로 된 숫자
#배열 두번째 값은 current_idx값으로 넣어 재사용
def bfs(number, current_idx):
    queue = []
    queue.append(1) #queue에는 나머지값
    remain_visited[1] = ['1', current_idx] # 0과 1로 된 숫자, 방문한 current_idx
    while queue:
        current_remain = queue.pop(0)
        if len(remain_visited[current_remain][0]) > 100:
            print("BARK")
            return
        for added in [0, 1]:
            next_remain = (current_remain * 10 + added) % number
            if next_remain == 0:
                print(remain_visited[current_remain][0] + str(added))
                return
            else:
                if remain_visited[next_remain][1] != current_idx:
                    remain_visited[next_remain][0] = remain_visited[current_remain][0] + str(added)
                    remain_visited[next_remain][1] = current_idx
                    queue.append(next_remain)                    


count = int(input())
nums = []
for i in range(count):
    nums.append(input())
current_idx = 0
for i in range(count):
    current_idx += 1
    if nums[i].count('1') + nums[i].count('0') == len(nums[i]):
        print(nums[i])
        continue
    bfs(int(nums[i]), current_idx)


#참조: https://westmino.tistory.com/4
    
