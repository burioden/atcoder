n, va, vb, l = map(int, input().split())

ans = l
for _ in range(n):
  x = ans / va
  y = x * vb
  ans = (ans + y) - ans
  
print(ans)
