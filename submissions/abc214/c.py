n = int(input())
s = list(map(int,input().split()))
t = list(map(int,input().split()))

dp = [10**9+1] * n
dp[0] = t[0]

for i in range(n*2):
  dp[(i+1)%n] = min(t[(i+1)%n],dp[i%n]+s[i%n])
  
print(*dp,sep="\n")
