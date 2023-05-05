n = int(input())
a = list(map(int,input().split()))

x = len(set(a))

if x == n:
  print('YES')
else:
  print('NO')
