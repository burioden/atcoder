n,m = map(int,input().split())
a = [list(map(int, input().split())) for _ in range(m)]

if n == 1:
  l = 0
  r = 10
elif n == 2:
  l = 10
  r = 100
elif n == 3:
  l = 100
  r = 1000

for i in range(l,r):
  for j in a:
    i = str(i)
    if i[j[0]-1] != str(j[1]):
      break
  else:
    print(i)
    exit()

print(-1)
