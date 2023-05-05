n = int(input())

cnt = 0
for i in range(60):
  if 2**i <= n:
    cnt += 1
  else:
    break

print(cnt-1)
