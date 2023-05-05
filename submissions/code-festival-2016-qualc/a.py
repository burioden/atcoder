s = input()

c = 101
f = -1

for i, d in enumerate(s):
  if d == 'C':
    c = min(c, i)
  elif d == 'F':
    f = max(f, i)
    
print('Yes' if c < f else 'No')
