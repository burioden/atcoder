import math

a,b = map(int,input().split())

c = pow(a,(2/3))
m = pow(2,(2/3)) * pow(b,(2/3))
x = math.floor(c / m)-1

if a < b + (a/2**0.5):
  print(a)
else:
  x1 = (b*(x)) + (a/((x+1)**0.5))
  x2 = (b*(x+1)) + (a/((x+2)**0.5))
  print(min(x1,x2))
