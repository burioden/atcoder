n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = 0
for i in b:
  i -= 1
  ans += a[i]
  
print(ans)
