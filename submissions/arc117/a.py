a,b = map(int,input().split())

x = ((max(a,b)+1)*max(a,b))//2
y = ((min(a,b)) * (min(a,b)-1))//2

god = []

if a > b:
  for i in range(1,a+1):
    god.append(i)
  for j in range(1,b):
    god.append(-j)
  god.append(-(x-y))
elif a < b:
  for i in range(1,b+1):
    god.append(-i)
  for j in range(1,a):
    god.append(j)
  god.append(x-y)
elif a == b:
  for i in range(1,b+1):
    god.append(i)
    god.append(-i)
    
print(*god)
