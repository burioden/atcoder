n = int(input())

for i in range(n):
  cnt = 0
  x = int(input())
  a = list(map(int,input().split()))
  for i in a:
    if i%2 == 1:
      cnt += 1
  print(cnt)
