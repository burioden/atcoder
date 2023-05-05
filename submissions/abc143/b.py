n = int(input())
d = list(map(int,input().split()))

ans = 0

for i in range(n):
  for l in range(i+1,n):
    ans += d[i]*d[l]

print(ans)
