s = int(input())

cnt = 0

if s == 1 or s == 2:
  print(4)
  exit()

while not s==1:
  cnt+=1
  if s%2 == 0:
    s = s/2
  else:
    s = 3*s+1

print(cnt+2)
