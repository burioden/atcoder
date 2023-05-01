n,w = map(int, input().split())
a = sorted(list(map(int, input().split())))

ans = []

for i in a:
  if i <= w:
    ans.append(i)

if a[0] < w:
  for i in range(n):
    for l in range(i+1,n):
      if ans[i] + ans[l] <= w:
          ans.append(ans[i] + ans[l])
      for k in range(l+1,n):
        if ans[i] + ans[l] + ans[k] <= w:
          ans.append(ans[i] + ans[l] + ans[k])

print(len(set(ans)))
