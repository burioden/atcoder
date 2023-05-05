n = int(input())
d,x = map(int,input().split())
a = [int(input()) for _ in range(n)]

y = 0

for i in a:
  for j in range(1,d+1):
    if (i * j)+1 <= d:
      y += 1

print(x+y+n)
