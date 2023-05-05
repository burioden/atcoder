n = input()
a = []
for i in range(len(n)):
  if n[i] == "1":
    a.append(0)
  else:
    a.append(1)
    
print(*a,sep="")
