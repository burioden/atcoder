h,w = map(int,input().split())
a = zip(*[input() for _ in range(h)])
b = zip(*[input() for _ in range(h)])

if sorted(a) == sorted(b):
  print('Yes')
else:
  print('No')
