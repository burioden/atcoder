'''
xを入れた状態の距離をとって、距離の最大公約数がdになる？
'''
import math
import functools
n,x = map(int,input().split())
a = sorted(list(map(int,input().split()))+[x])

kyori = []
for i in range(1,n+1):
  kyori.append(a[i]-a[i-1])
  
kyori.sort()

d = functools.reduce(math.gcd, kyori)

print(d)
