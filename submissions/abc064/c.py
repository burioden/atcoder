n = int(input())
a = list(map(int,input().split()))

c = [0]*8
r = 0

for i in a:
  if 3200 <= i:
    r += 1
  elif 2800 <= i:
    c[7] = 1
  elif 2400 <= i:
    c[6] = 1
  elif 2000 <= i:
    c[5] = 1
  elif 1600 <= i:
    c[4] = 1
  elif 1200 <= i:
    c[3] = 1
  elif 800 <= i:
    c[2] = 1
  elif 400 <= i:
    c[1] = 1
  else:
    c[0] = 1


mi = sum(c) if sum(c) > 0 else 1
ma = sum(c) + r

print(mi,ma)
