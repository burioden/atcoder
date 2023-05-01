x,y,n = map(int, input().split())

if y > x*3:
  print(n*x)
else:print((n//3)*y+(n%3)*x)
