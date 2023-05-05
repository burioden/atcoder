a = set(list(map(int,input().split())))
b = set(list(map(int,input().split())))

if 1 <= len(a&b):
  print('YES')
else:
  print('NO')
