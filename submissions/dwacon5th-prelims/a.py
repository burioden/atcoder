n = int(input())
a = list(map(int, input().split()))
m = sum(a)/n

ans = []

for i, d in enumerate(a):
  x = abs(m - d)
  ans.append([x, i])

ans.sort()

print(ans[0][1])
