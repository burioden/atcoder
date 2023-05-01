x,y = map(int, input().split())
ans = int(((y-x) + (10-1)) / 10)
if x < y:
  print(ans)
else:
  print(0)
