n,x = map(int,input().split())
a = sorted(list(map(int,input().split())))

cnt = 0
for i in range(n):
  x -= a[i]
  if 0 <= x:
    cnt += 1
  else:
    break

print(cnt-1 if x > 0 else cnt)
