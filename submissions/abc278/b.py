h,m = map(int,input().split())

while True:
  if 0 <= h <= 5 or 10 <= h <= 15:
    break
  elif 20 <= h <= 23 and 0 <= m <= 39:
    break
  elif 6 <= h <= 9 or 16 <= h <= 19:
    h = (h+1) % 24
    m = 0
  elif 20 <= h <= 23 and 40 <= m <= 59:
    if m == 59:
      h = (h+1) % 24
      m = 0
      if 0 <= h <= 5 or 10 <= h <= 15 or 20 <= h <= 23:
        break
    else:
      m = (m+1) % 60
      
print(h,m)
