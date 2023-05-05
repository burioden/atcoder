h, w = map(int, input().split())
a = [input() for _ in range(h)]

for i in a:
  print(i.replace('TT', 'PC'))
