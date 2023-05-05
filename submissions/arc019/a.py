s = input()

d = {'O': 0, 'I': 1, 'Z': 2, 'S': 5, 'D': 0, 'B': 8}

for i in s:
  if i in d:
    print(d[i], end='')
  else:
    print(i, end='')
    
print()
