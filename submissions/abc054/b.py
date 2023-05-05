n,m = map(int,input().split())
a = [input() for _ in range(n)]
b = [input() for _ in range(m)]

for i in a:
  for j in b:
    if j not in i:
      print('No')
      exit()

print('Yes')
