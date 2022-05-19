from copy import deepcopy
n = int(input())
init = list(map(int,input()))
final = list(map(int,input()))

def change_first(light):
    #print(light)
    count = 0
    light[0] = 1 - light[0]
    light[1] = 1 - light[1]
    count += 1

    for i in range(1, n):
        if light[i-1] == final[i-1]:
            continue
        count += 1
        light[i-1] = 1 - light[i-1]
        light[i] = 1 - light[i]
        if i+1 < n:
            light[i+1] = 1 - light[i+1]
    
    for i in range(n):
        if light[i] != final[i]:
            return 1e6
    return count
             
def non_change_first(light):
    #print(light)
    count = 0
    for i in range(1, n):
        if light[i-1] == final[i-1]:
            continue
        count += 1
        light[i-1] = 1 - light[i-1]
        light[i] = 1 - light[i]
        if i+1 < n:
            light[i+1] = 1 - light[i+1]
    for i in range(n):
        if light[i] != final[i]:
            return 1e6
    return count

count1 = change_first(deepcopy(init))
count2 = non_change_first(deepcopy(init))
result = min(count1, count2)
if result == 1e6:
    result = -1
print(result)

#참고: https://javaiyagi.tistory.com/593