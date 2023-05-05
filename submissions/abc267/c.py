n,m = map(int,input().split())
a = list(map(int,input().split()))

s = sum(a[i] * (i+1) for i in range(m))
t = sum(a[:m])
# print(s,t)
ans = s

# この部分の挙動、わからなー
for i in range(n-m):
  s -= t - a[i+m] * m
  # print(s)
  t -= a[i] - a[i+m]
  # print(t)
  ans = max(ans,s)
  
print(ans)
