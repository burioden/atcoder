x = int(input())

ans = 0
if 1800 <= x:
  ans = 1
elif 1600 <= x:
  ans = 2
elif 1400 <= x:
  ans = 3
elif 1200 <= x:
  ans = 4
elif 1000 <= x:
  ans = 5
elif 800 <= x:
  ans = 6
elif 600 <= x:
  ans = 7
elif 400 <= x:
  ans = 8
  
print(ans)
