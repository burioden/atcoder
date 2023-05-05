d = list(map(int,input().split()))
j = list(map(int,input().split()))

ans = 0
for i in range(7):
  if d[i] >= j[i]:
    ans += d[i]
  else:
    ans += j[i]
    
print(ans)
