'''
2進数で考えた
・110を逆にする
  0 -> 1が0こ
  1 -> 2(2^1)が1こ
  1 -> 4(2^2)が1こ 合計で6
'''

s = list(input())[::-1]

n = len(s)
ans = 0

for i in range(n):
  ans += (26 ** i) * (ord(s[i]) - 64)
  
print(ans)
