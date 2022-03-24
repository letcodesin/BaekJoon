N = int(input())
t = []
p = []
for i in range(N):
    t1, p1 = map(int, input().split())
    t.append(t1)
    p.append(p1)
dp = [0]*(N+1) #i번째 날까지 일했을때 최댓값
#날짜를 역순으로해서 dp를 계산해야 가능한 모든 경우의 수 체크 가능
for i in range(len(t)-1, -1, -1): #len(t)-1부터 0까지 -1씩 감소하면서 역순
    if t[i] + i <= N:
        dp[i] = max(p[i]+dp[(t[i]+i)], dp[i+1])
    else:
        dp[i] = dp[i+1]
#print(t)
#print(p)
#print(dp)
print(dp[0])

#참고: https://jrc-park.tistory.com/119

############################wrong solution############################
#반례: 다음날 수익이 높아 하루 쉬고 그것을 선택한 경우
N = int(input())
days = []
for i in range(N):
    t, p = map(int, input().split())
    days.append((t, p))
print(days)
days.append((1,0))

max_money = 0
for i in range(N):
    current_day = i + days[i][0]
    money = 0
    if current_day <= N:
        money += days[i][1]
        while current_day + days[current_day][0] <= N:
            money += days[current_day][1]
            current_day += days[current_day][0]

    print(money)
    if money > max_money:
        max_money = money

print(max_money)