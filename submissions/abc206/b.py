n = int(input())

cnt = 0
yen = 0

for i in range(n):
  yen += i
  if yen >= n:
    break
  else:
    cnt += 1

print(cnt)
