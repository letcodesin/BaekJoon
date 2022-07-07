#스위핑 알고리즘-stack, 분할정복
n = int(input())
marea = 0
stack = []
histogram = []

for _ in range(n):
    histogram.append(int(input()))

for i in range(n):
    #print(stack)
    while stack and histogram[stack[-1]] > histogram[i]:
        height = histogram[stack[-1]]
        stack.pop()
        #print(stack)
        width = i
        if stack:
            width = i - stack[-1] -1
        marea = max(marea, width * height)
        #print("marea: ", marea)
    stack.append(i)
    
while stack:
    #print("while stack: ",stack)
    height = histogram[stack[-1]]
    stack.pop()
    width = n
    if stack:
        width = n - stack[-1] -1
    marea = max(marea, width * height)
    #print("width*height:", width*height)
print(marea)

#참고: https://private-space.tistory.com/12
# https://derekahndev.github.io/problem%20solving/boj-1725/
'''
############################시간초과 풀이#########################
n = int(input())
histogram = []
for _ in range(n):
    histogram.append(int(input()))

marea = 0
for i in range(n):
    key_length = histogram[i]
    left = i
    right = i
    #왼쪽으로 갈 수 있는 거리
    while left >= 0 and key_length <= histogram[left]:
        left -= 1
    #오른쪽으로 갈 수 있는 거리
    while right < n and key_length <= histogram[right]:
        right += 1
    marea = max(marea, key_length*(right-left-1))
    #print(histogram[i], left, right, key_length*(right-left-1))

print(marea)
'''