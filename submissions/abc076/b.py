n = int(input())
k = int(input())

ans = 1
cnt = 0

while cnt != n:
  if ans < k:
    ans *= 2
    cnt += 1
  else:
    ans += k
    cnt += 1

print(ans)
