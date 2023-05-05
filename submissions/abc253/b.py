h, w = map(int, input().split())
g = [input() for _ in range(h)]

maru = []

for i in range(h):
  for j in range(w):
    if g[i][j] == 'o':
      maru.append([i, j])

ans = abs(maru[0][0] - maru[1][0]) + abs(maru[0][1] - maru[1][1])

print(ans)
