a,b,c = map(int, input().split())

if c-1 <= a+b:
  print(c+b)
else:
  print(a+2*b+1)
