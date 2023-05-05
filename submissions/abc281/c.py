n,t = map(int,input().split())
a = list(map(int,input().split()))

s = sum(a)
now = t%s
track = 0
for i in a:
  if now >= i:
    now -= i
    track += 1
  else:
    track += 1
    break

print(track,now)
