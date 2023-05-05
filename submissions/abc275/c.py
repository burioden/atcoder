s = [input() for _ in range(9)]
ans = 0

for r in range(1,9):
  for i in range(9-r):
    for j in range(9-r):
      for ri in range(r):
        if s[i+ri][j] + s[i][j+r-ri]+s[i+r][j+ri]+s[i+r-ri][j+r] == "####":
          ans += 1

print(ans)
