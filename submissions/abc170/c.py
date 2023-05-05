x,n = map(int, input().split())
a = sorted(set(map(int,input().split())))

ans = []
if x not in a:
  print(x)
  exit()
else:
  i = 1
  j = 0
  while j <= 2:
    if x-i not in a:
      ans.append(x-i)
      j += 1
    if x+i not in a:
      ans.append(x+i)
      j += 1
    i += 1

b = []
for i,d in enumerate(ans):
  k = abs(x-d)
  b.append([k,d])
  
print(sorted(b)[0][1])
