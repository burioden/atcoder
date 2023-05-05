n = int(input())
h = list(map(int,input().split()))

cnt = 0
x = 0
for i in range(1,n):
  if h[i-1] >= h[i]:
    x += 1
    cnt = max(cnt,x)
  else:
    x = 0

print(cnt)
