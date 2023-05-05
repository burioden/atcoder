a, b = input().split()

aans = 0
for i in a:
  aans += int(i)
  
bans = 0
for i in b:
  bans += int(i)
  
print(max(aans, bans))
