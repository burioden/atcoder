o = input()
e = input()

li = []
for i in range(len(e)):
  x,y = o[i],e[i]
  li.append(x+y)

if len(e) < len(o):
  print(*li,o[-1],sep="")
else:
  print(*li,sep="")
