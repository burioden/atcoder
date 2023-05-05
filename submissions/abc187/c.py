n = int(input())
a = set()
b = set()
for i in range(n):
  s = input()
  if s[0] == '!':
    b.add(s[1:])
  else:
    a.add(s)
    
c = a&b

if len(c) == 0:
  print('satisfiable')
else:
  print(list(c)[0])
