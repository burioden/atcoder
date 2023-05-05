s = input()

ans = 0
for i,d in enumerate(s):
  if d == 'a':
    ans = max(i+1,ans)

print(ans if ans > 0 else -1)
