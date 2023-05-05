x,y = map(int, input().split())
l = [0,1,2]
ll = [x,y]
if x == y:
  print(x)
else:
  s = set(l)^set(ll)
  print(''.join(map(str, s)))
