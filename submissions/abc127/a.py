a,b = map(int, input().split())

if a < 6:
  ans = 0
elif a < 13:
  ans = b//2
else:
  ans = b

print(ans)
