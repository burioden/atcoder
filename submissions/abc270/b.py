goal,wall,hammer = map(int, input().split())

ans = 0

# できないパターン
if (0 < wall < goal < hammer or 0 < wall < hammer < goal or 0 > wall > goal > hammer or 0 > wall > hammer > goal):
  ans = -1
# ハンマーあればできるパターン
elif 0 < wall < goal or 0 > wall > goal:
  if hammer < 0 < wall < goal or hammer > 0 > wall > goal:
    ans = abs(hammer*2)+abs(goal) 
  else:
    ans = abs(goal)
else:
  ans = abs(goal)

print(ans)
