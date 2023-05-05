h,w = map(int,input().split())

if h == 1 or w == 1:
  print(1)
elif h%2 == 0:
  h //= 2
  print(h*w)
else:
  h //= 2
  h1 = h+1
  if w%2 == 0:
    w //= 2
    print((h*w)+(h1*w))
  else:
    w //= 2
    w1 = w+1
    print((h*w)+(h1*w1))
