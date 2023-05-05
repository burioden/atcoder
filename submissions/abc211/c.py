s = input()

c ='chokudai'
MOD = 1000000007

dp = [0] * 9
dp[0] = 1

for i in s:
  for j, d in enumerate(c):
    if i == d: # 今見てる文字と、cの一部が一致したら
      dp[j + 1] += dp[j] # 前までこれた結果をプラスする
      dp[j + 1] %= MOD # modとる

print(dp[-1] % MOD)
