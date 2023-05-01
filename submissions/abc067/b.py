n,k = map(int, input().split())
li= map(int, input().split())

nl = sorted(li,reverse=1)
ans = 0

for i in range(k):
  ans += nl[i]

print(ans)
