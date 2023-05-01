a,b,x = map(int, input().split())

ok = 0
ng = 10**9+1

while ng-ok > 1:
  n = (ok + ng)//2
  d = len(str(n))
  if a*n + b*d <= x:
    ok = n
  else:
    ng = n

print(ok)
