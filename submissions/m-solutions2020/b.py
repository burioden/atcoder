a,b,c = map(int, input().split())
k = int(input())

cnt = 0

while b <= a:
  cnt += 1
  b*=2

while c <= b:
  cnt += 1
  c*=2

if cnt <= k:
  print('Yes')
else:
  print('No')
