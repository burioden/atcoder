s = input()
t = 'CODEFESTIVAL2016'

nya = 0
for i in range(16):
  if s[i] != t[i]:
    nya += 1
    
print(nya)
