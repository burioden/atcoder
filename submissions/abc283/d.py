s = input()

a = set()

for i in s:
  if i == ')':
    a = set()
  elif i in a:
    print('No')
    exit()
  elif i == '(':
    continue
  else:
    a.add(i)
    
print('Yes')
