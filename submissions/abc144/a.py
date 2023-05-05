a, b = map(int, input().split())

if a > 9 or b > 9:
  ans = -1
else:
  ans = a * b

print(ans)
