l,h = map(int,input().split())
n = int(input())
for i in range(n):
  a = int(input())
  if l <= a <= h:
    print(0)
  elif a < l:
    print(l-a)
  else:
    print(-1)
