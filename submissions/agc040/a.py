s = input()

n = len(s)
ans = [0]*(n+1)

for i in range(n):
  if s[i] == "<":
    ans[i+1] = max(ans[i+1],ans[i]+1)

for i in reversed(range(n)):
  if s[i] == ">":
    ans[i] = max(ans[i],ans[i+1]+1)

print(sum(ans))
