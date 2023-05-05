n,k = map(int,input().split())
h = list(map(int,input().split()))

dp = [10**5] * n
dp[0] = 0
dp[1] = abs(h[1]-h[0])

for i in range(2,n):
  dp[i] = dp[i-1] + abs(h[i] - h[i-1])
  for j in range(2,k+1):
    if i - j >= 0:
      dp[i] = min(abs(h[i]-h[i-j]) + dp[i-j], dp[i])

print(dp[-1])
