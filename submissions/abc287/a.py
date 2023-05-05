n = int(input())
a = [input() for _ in range(n)]

x = a.count('For')

if x >= (n+1)//2:
  print('Yes')
else:
  print('No')
