n,m,t = map(int,input().split())
a = list(map(lambda x: int(x)*-1,input().split()))
s = [list(map(int,input().split())) for _ in range(m)]

for i in s:
  a[i[0]-1] += i[1]

for i in range(n-1):
  t += a[i]
  if t < 1:
    print('No')
    exit()

print('Yes')
