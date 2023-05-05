x,y = map(int,input().split())

cnt = 0

while x <= y:
  x *= 2
  cnt += 1

print(cnt)
