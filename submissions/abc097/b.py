n = int(input())

ans = 1
for i in range(2,11):
  for j in range(2,32):
    if j**i <= n:
      ans = max(ans,j**i)

print(ans)
