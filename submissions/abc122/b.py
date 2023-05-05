s = list(input())
a = list("ACGT")

cnt = 0
ans = 0

for i in s:
  if i in a:
    cnt += 1
    ans = max(cnt,ans)
  else:
    cnt = 0

print(ans)
