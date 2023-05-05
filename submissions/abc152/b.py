a,b = map(int,input().split())

ab = str(a)*b
ba = str(b)*a

if ab < ba:
  print(ab)
else:
  print(ba)
