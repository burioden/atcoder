w,a,b = map(int, input().split())

if w < abs(a-b):
  print(abs(a-b)-w)
else:
  print(0)
