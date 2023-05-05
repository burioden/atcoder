k,n = map(int,input().split())
a = list(map(int,input().split()))

ans = k - max(a) + min(a)

for i in range(1,n):
  if ans < a[i] - a[i-1]:
    ans = a[i] - a[i-1]

print(k - ans)
