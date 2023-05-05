n,d = map(int,input().split())
x = [list(map(int, input().split())) for _ in range(n)]

ans = 0

def f(n):
    flg = False
    if n == 1 or n == 0:
      flg = True
    for i in range(1,n):
        if i*i == n:
            flg = True
            break
    return flg

for i in range(n):
  for j in range(i):
    if f(sum([(x[i][l]-x[j][l])**2 for l in range(d)])):
      ans += 1

print(ans)
