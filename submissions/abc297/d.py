a, b = sorted(map(int, input().split()))

if a == b:
  exit(print(0))

cnt = 0

while b != a:
  if b % a != 0:
    cnt += b // a
    b = b % a
    a, b = b, a
  else:
    cnt += (b // a) - 1
    break

print(cnt)
