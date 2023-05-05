'''
悩み
・最初、全て登れないとして考えるのか、全て登れるとして考えるのかが ぬぬ となる
・bitのor,and,xorを脳に叩き込みたい
・setにしようぜ…
'''

n = int(input())
a = set(map(int, input().split()))
m = int(input())
b = set(map(int, input().split()))
x = int(input())

dp = [0] * (x + 1)
dp[0] = 1 # 0段目は既にいるから絶対にTrue（登れる）
  
for i in range(x):
  if i in b:
    dp[i] = 0 # もちがあったら登れない
  for j in a:
    if (i + j) not in b and (i + j) <= x: # 今いるところと、各歩数について
      dp[i + j] |= dp[i] # ひとつでも登ってこれる方法があれば（Trueの箇所があれば）True
      
print('Yes' if dp[x] else 'No')
