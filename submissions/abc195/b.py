import math
a,b,w = map(int, input().split())
u = int(1000*w//a)
l = int(math.ceil(1000*w/b))
if u < l:
  print("UNSATISFIABLE")
else:
  print(l,u)
