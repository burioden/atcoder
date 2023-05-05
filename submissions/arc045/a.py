a = list(input().split())
b = []

for i in a:
  if i == 'Right':
    b.append('>')
  elif i == 'Left':
    b.append('<')
  else:
    b.append('A')
    
print(*b)
