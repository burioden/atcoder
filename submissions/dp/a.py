n = int(input())
h = list(map(int,input().split()))

dp = [10**5] * n
dp[0] = 0
dp[1] = abs(h[1]-h[0])

for i in range(2,n):
  dp[i] = min(abs(h[i] - h[i-1]) + dp[i-1],
              abs(h[i] - h[i-2]) + dp[i-2])
  
print(dp[-1])
