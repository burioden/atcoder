k,s = map(int,input().split())

cnt = 0
for x in range(k+1):
  for y in range(k+1):
    z = s-(x+y)
    if x + y + z == s and 0 <= z <= k:
      cnt += 1

print(cnt)
