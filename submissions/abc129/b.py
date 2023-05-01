n = int(input())
li = list(map(int, input().split()))

for i in range(1,n):
  li[i] += li[i-1]

ans = 100000

for t in range(n):
  s1 = li[t]
  s2 = li[n-1] - s1
  if abs(s1 - s2) < ans:
    ans = abs(s1 - s2)

print(ans)
