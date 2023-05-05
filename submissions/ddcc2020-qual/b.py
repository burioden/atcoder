n = int(input())
a = list(map(int,input().split()))
m = sum(a)

ans = m
s = 0

for i in range(n):
  s += a[i]
  ans = min(ans, abs(s - (m-s)))

print(ans)
