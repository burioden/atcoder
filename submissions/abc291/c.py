n = int(input())
s = input()

visited = set()
x, y = 0, 0
visited.add((x, y))

for i in s:
  if i == 'R':
    x += 1
    visited.add((x, y))
  elif i == 'L':
    x -= 1
    visited.add((x, y))
  elif i == 'U':
    y += 1
    visited.add((x, y))
  elif i == 'D':
    y -= 1
    visited.add((x, y))

print('No' if len(visited) == n + 1 else 'Yes')
