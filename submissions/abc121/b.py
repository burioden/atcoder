n,m,c = map(int, input().split())
b = list(map(int, input().split()))
a = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
ans = []

for i in range(n):
  l = []
  for k in range(m):
    l.append(a[i][k]*b[k])
  ans.append(l)


for i in range(n):
  if sum(ans[i])+c > 0:
    cnt += 1

print(cnt)
