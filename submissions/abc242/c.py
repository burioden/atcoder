'''
例えば4桁の場合、1桁目を5にして樹形図を作ると、1と9に向かって合計数が収縮していく
までは考察できたが、こういうやつはdpでできるのか…すごい
'''

n = int(input())

mod = 998244353

# n+1個のdpテーブルを作る
dp = [[0 for _ in range(10)] for _ in range(n+1)]
# dpテーブルのセット
for i in range(1,10):
  dp[1][i] = 1

# iが桁数、jが1-9
for i in range(2,n+1):
  for j in range(1,10):
    if j == 1:
      dp[i][j] = dp[i-1][j] + dp[i-1][j+1]
    elif j == 9:
      dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
    else:
      dp[i][j] = dp[i-1][j-1] + dp[i-1][j] + dp[i-1][j+1]
    #必ずmodとってあげる
    dp[i][j] %= mod 
      
print(sum(dp[n])%mod)
