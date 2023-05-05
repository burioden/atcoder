h,w,x,y = map(int,input().split())
s = [input() for _ in range(h)]

x -= 1
y -= 1

cnt = 0

for i in range(x+1,h):
  if s[i][y] == ".":
    cnt += 1
  else:
    break

for i in reversed(range(0,x)):
  if s[i][y] == ".":
    cnt += 1
  else:
    break

for i in range(y+1,w):
  if s[x][i] == ".":
    cnt += 1
  else:
    break

for i in reversed(range(0,y)):
  if s[x][i] == ".":
    cnt += 1
  else:
    break

print(cnt+1)
