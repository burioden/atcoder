n = int(input())
a,b = map(int,input().split())
k = int(input())
p = list(map(int,input().split()))

p.append(a)
p.append(b)

if len(p) == len(set(p)):
  print('YES')
else:
  print('NO')
