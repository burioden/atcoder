n = int(input())
s = list(map(int,input().split()))

cnt = 0
for i in s:
  flg = 0
  for a in range(1,1001):
    for b in range(1,1001):
      if 4*a*b+3*a+3*b == i:
        flg = 1
  if not flg:
    cnt += 1

print(cnt)
