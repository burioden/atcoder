'''
ソートしていれる!
0〜n+1をセットし、r = a[i] , l = a[i-1] とし、距離の最小 = kをとる
kyoriに距離を入れてく
割り算すればいけそう 計算量はO(N)？うーん
最大値を気をつけよう
'''

n,m = map(int,input().split())
a = sorted(list(map(int,input().split()))+[n+1]+[0])

k = 10**10
kyori = []

if m == 0:
  print(1)
  exit()

for i in range(1,m+2):
  r = a[i]
  l = a[i-1]
  if r-l == 1:
    continue
  else:
    k = min((r-l)-1,k)
    kyori.append((r-l)-1)

if sum(a) == 0:
  print(0)
  exit()
  
ans = 0
for i in kyori:
  if i%k != 0:
    ans += (i//k)+1
  else:
    ans += i//k
    
print(ans)
