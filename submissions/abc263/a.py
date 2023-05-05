a,b,c,d,e = map(int, input().split())

g = sorted([a,b,c,d,e])

flg = 0

if g[0] == g[1] == g[2]:
  if g[3] == g[4]:
    flg = 1
elif g[0] == g[1]:
  if g[2] == g[3] == g[4]:
    flg = 1

print('Yes' if flg else 'No')
