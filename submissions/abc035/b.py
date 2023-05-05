s = list(input())
n = int(input())

u = s.count("U")
d = s.count("D")
l = s.count("L")
r = s.count("R")
q = s.count("?")

x = abs(l-r)
y = abs(u-d)

if n == 1:
  print(x+y+q)
else:
  if x+y > q:
    print(x+y-q)
  else:
    print(len(s)%2)
