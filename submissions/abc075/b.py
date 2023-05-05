DXY = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(1,-1),(-1,-1),(-1,1)]

h,w = map(int,input().split())
s = [list(input()) for _ in range(h)]

s = [[0 if i == "." else "#" for i in r] for r in s]

for i in range(h):
  for j in range(w):
    if s[i][j] == "#":
      continue
    for k in DXY:
      # 難関だった…iは高さ、jは幅、と考えりゃそりゃそうだった
      ni,nj = k[1] + i, k[0] + j

      if ni < 0 or ni >= h or nj < 0 or nj >= w:
        continue

      if s[ni][nj] == "#":
        s[i][j] += 1

for r in s:
  print(*r,sep="")
