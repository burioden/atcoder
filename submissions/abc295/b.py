r, c = map(int, input().split())
b = [input() for _ in range(r)]

for i in range(r):
  for j in range(c):
    bb = b[i][j]
    for k in range(r):
      for l in range(c):
        if b[k][l].isdigit():
          d = int(b[k][l])
        else:
          d = -1
        if abs(i - k) + abs(j - l) <= d:
          bb = '.'
    print(bb, end='')
  print()
