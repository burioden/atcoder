n, m = map(int, input().split())
h = list(map(int, input().split()))

flg = [1 for _ in range(n)]
  
for _ in range(m):
  a, b = map(int, input().split())
  a -= 1
  b -= 1
  if h[a] <= h[b]:
    flg[a] = 0
  if h[b] <= h[a]: # ここをelifで書いていたから40分苦しんだ
    flg[b] = 0

print(sum(flg))
