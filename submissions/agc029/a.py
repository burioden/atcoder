s = input()

cnt = 0
ans = 0

for i,d in enumerate(s):
  if d == "W":
    ans += i-cnt
    cnt += 1

print(ans)
